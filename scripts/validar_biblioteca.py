#!/usr/bin/env python3
"""Check local Markdown/YAML, relative paths, formula delimiters and exercise IDs.

Run: python3 scripts/validar_biblioteca.py
Requires PyYAML. This is not a proof checker or a MathJax rendering test.
No network access or writes are performed.
"""
from pathlib import Path
from urllib.parse import unquote,urlsplit
import datetime,hashlib,json,re,subprocess,yaml
repo=Path(__file__).resolve().parents[1];vault=repo/'Matematicas-UPM'
errors=[];counts={'markdown':0,'vault_yaml':0,'relative_links':0,'source_paths':0,'math_fragments':0,'units':0,'paired_exercises':0,'learning_notes':0,'pdf_integrity_checks':0}
required={'title','subject','tema','type','language','status','tags','sources','updated'}
study={'definition','theorem','proof','example','exercises','review'}
class Loader(yaml.SafeLoader):pass
def mapping(loader,node,deep=False):
 result={}
 for kn,vn in node.value:
  key=loader.construct_object(kn,deep=deep)
  if key in result:raise ValueError(f'duplicate key {key}')
  result[key]=loader.construct_object(vn,deep=deep)
 return result
Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
def check(ok,msg):
 if not ok:errors.append(msg)
for p in sorted(repo.rglob('*.md')):
 if '.git' in p.parts:continue
 counts['markdown']+=1;rel=str(p.relative_to(repo))
 try:text=p.read_text(encoding='utf-8',errors='strict')
 except UnicodeDecodeError as e:errors.append(f'{rel}: {e}');continue
 check(text.endswith('\n'),rel+': final newline missing')
 check(bool(text.strip()),rel+': empty file')
 check(p.name.isascii() and ' ' not in p.name,rel+': Markdown filename')
 body=text
 if p.is_relative_to(vault):
  match=re.match(r'\A---\n(.*?)\n---\n',text,re.S)
  check(match is not None,rel+': YAML missing')
  if match:
   body=text[match.end():]
   try:
    meta=yaml.load(match.group(1),Loader=Loader)
    check(isinstance(meta,dict) and required<=meta.keys(),rel+': metadata incomplete')
    check(meta.get('language')=='es-zh',rel+': language')
    check(meta.get('status') in {'complete','partial','pending_review'},rel+': status')
    check(meta.get('type') in study|{'guide','index','tracking','rules'},rel+': type')
    check(isinstance(meta.get('updated'),datetime.date),rel+': date')
    check(isinstance(meta.get('tags'),list),rel+': tags')
    check(isinstance(meta.get('sources'),list),rel+': sources')
    if meta.get('type') in study:
     counts['learning_notes']+=1
     check(bool(meta.get('sources')),rel+': study note has no verified sources')
     check(bool(re.search(r'[\u4e00-\u9fff]',body)),rel+': Chinese missing')
     check(bool(re.search(r'\b(Español|español|española|Explicación|Análisis|Estrategia|ES)\b',body)),rel+': explicit Spanish explanation label missing')
    for source in meta.get('sources',[]):
     target=(p.parent/source).resolve()
     check(not Path(source).is_absolute() and target.is_relative_to(vault) and target.is_file(),rel+': missing/external source '+source)
     counts['source_paths']+=1
    counts['vault_yaml']+=1
   except (ValueError,TypeError,yaml.YAMLError) as e:errors.append(f'{rel}: YAML {e}')
 prose=re.sub(r'(?ms)^```.*?^```[^\n]*\n?', '',body)
 prose=re.sub(r'`[^`\n]*`','',prose)
 check('[[' not in prose,rel+': wikilink')
 for target in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]*)\)',prose):
  if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',target):continue
  parsed=urlsplit(target);decoded=unquote(parsed.path)
  check(not parsed.fragment,rel+': anchor not checked '+target)
  resolved=(p.parent/decoded).resolve()
  check(not Path(decoded).is_absolute() and resolved.is_relative_to(vault if p.is_relative_to(vault) else repo),rel+': link escapes root '+target)
  check(resolved.is_file(),rel+': broken link '+target)
  counts['relative_links']+=1
 headings=re.findall(r'^(#{1,6})\s+.+$',prose,re.M)
 check(headings.count('#')==1,rel+': H1 count')
 previous=0
 for h in headings:check(len(h)<=previous+1,rel+': skipped heading level');previous=len(h)
 # Basic source-level checks only; not a MathJax render or proof checker.
 tokens=list(re.finditer(r'(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$|(?<!\\)\$[^\n$]*?(?<!\\)\$',prose))
 remainder=re.sub(r'(?<!\\)\$\$[\s\S]*?(?<!\\)\$\$|(?<!\\)\$[^\n$]*?(?<!\\)\$','',prose)
 check(not re.search(r'(?<!\\)\$',remainder),rel+': unmatched dollar delimiter')
 for m in tokens:
  counts['math_fragments']+=1
  math=m.group();depth=0
  for c in re.findall(r'(?<!\\)[{}]',math):
   depth+=1 if c=='{' else -1
   check(depth>=0,rel+': negative brace balance')
  check(depth==0,rel+': unbalanced braces')
  stack=[]
  for action,environment in re.findall(r'\\(begin|end)\{([^}]+)\}',math):
   if action=='begin':stack.append(environment)
   else:
    check(bool(stack) and stack[-1]==environment,rel+': environment mismatch')
    if stack:stack.pop()
  check(not stack,rel+': unclosed environment')


# Pair exercise headings with solution headings, independently of body references.
for theory in sorted((vault/'01_Algebra').rglob('01_Teoria_Demostraciones.md')):
 unit=theory.parent
 q=unit/'05_Ejercicios.md';a=unit/'06_Soluciones.md'
 check(q.is_file() and a.is_file(),str(unit)+': exercise files missing')
 if not q.is_file() or not a.is_file():continue
 pattern=r'^## (A\d+-E\d+)\b'
 questions=re.findall(pattern,q.read_text(),re.M)
 answers=re.findall(pattern,a.read_text(),re.M)
 check(bool(questions) and questions==answers,str(unit)+': question/solution IDs differ')
 check(len(questions)==len(set(questions)),str(unit)+': duplicate exercise IDs')
 counts['units']+=1;counts['paired_exercises']+=len(questions)
# Check received originals against the recorded SHA-256, without touching them.
catalog=(vault/'00_Fuentes/00_Catalogo_Fuentes.md').read_text()
for source_id,digest in re.findall(r'\| (AL-[A-Z]+-\d+) \| \d+ \| `([0-9a-f]{64})` \|',catalog):
 candidates=list((vault/'00_Fuentes/Algebra_Lineal'/source_id).glob('*.pdf'))
 check(len(candidates)==1,source_id+': unique original missing')
 if len(candidates)==1:
  check(hashlib.sha256(candidates[0].read_bytes()).hexdigest()==digest,source_id+': original hash changed')
 counts['pdf_integrity_checks']+=1
check(counts['pdf_integrity_checks']==6,'six PDF integrity records expected')
requirements=vault/'99_Seguimiento/00_Requisitos_Originales.txt'
check(hashlib.sha256(requirements.read_bytes()).hexdigest()=='aed25f94f64ced88451867a92a60c2db95a89c32c0df57c6cd843fbb1451a94a','requirements changed')
result={'counts':counts,'errors':errors,'passed':not errors,'scope':'UTF-8, YAML, paths, exercise IDs, basic formula delimiters and original hashes; no automated proof checking or GUI rendering.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
