#!/usr/bin/env python3
"""Reproduce 132 exact checks of the worked linear algebra calculations.

Run from any directory: python3 scripts/comprobar_calculos_algebra.py
Requires SymPy. No network access or writes; not a general proof checker.
"""
import json
import sympy as s
M=s.Matrix;R=s.Rational;t,x,y,z,a,b,c,k=s.symbols('t x y z a b c k')
checks=[]
def eq(actual,expected,label):
 if isinstance(actual,s.MatrixBase):ok=actual.shape==expected.shape and (actual-expected).applyfunc(s.simplify)==s.zeros(*actual.shape)
 elif isinstance(actual,(tuple,list)):ok=actual==expected
 else:ok=s.simplify(actual-expected)==0
 checks.append({'label':label,'passed':bool(ok)})
 if not ok:print('FAIL',label,actual,expected)
def null(A,v,label):eq(A*v,s.zeros(A.rows,v.cols),label)
# Elementary independent checks by entries, exact solves, ranks and nullspaces.
U=M([[1,1],[0,1]]);W=M([[1,0],[1,1]])
eq(U*W,M([[2,1],[1,1]]),'2.1 GL2 AB');eq(W*U,M([[1,1],[1,2]]),'2.1 GL2 BA')
eq(U.inv(),M([[1,-1],[0,1]]),'2.1 GL2 inverse A');eq(W.inv(),M([[1,0],[-1,1]]),'2.1 GL2 inverse B')
null(M([[1,-2,1]]),M([[2,-1],[1,0],[0,1]]),'2.2 plane parametrization')
null(M([[1,1,0],[0,1,-1]]),M([-1,1,1]),'2.2 E02 kernel')
eq(M([[1,0,1],[0,1,1],[1,1,2]]).rank(),2,'2.3 dependent plane rank')
eq(M([[1,0],[0,1],[1,1]])*M([1,2]),M([1,2,3]),'2.3 combination')
eq(M([[1,1],[1,-1]]).inv()*M([c,t]),M([(c+t)/2,(c-t)/2]),'2.3 polynomial coefficients')
eq(M([[1,0,0],[0,1,0],[1,1,1]]).det(),1,'2.4 extraction is basis')
eq(M([[1,0,1],[1,1,0],[0,1,0]]).det(),1,'2.4 completion independent')
eq(M([[1,0,1],[1,1,0],[0,1,0]])*M([y-z,z,x-y+z]),M([x,y,z]),'2.4 completion coordinates')
P=M([[1,-1],[2,1]])
eq(P.inv()*M([0,3]),M([1,1]),'2.5 source coordinates')
eq(P.inv()*M([x,y]),M([(x+y)/3,(y-2*x)/3]),'2.5 general coordinates')
A=M([[1,-1,1],[2,-2,2]]);G=M([[1,-1],[1,0],[0,1]])
eq(A.rank(),1,'2.5 repeated equation rank');null(A,G,'2.5 generators in kernel');eq(G.rank(),2,'2.5 independent generators')
G=M([[1,0,1],[0,1,1],[1,0,1],[0,1,1]]);A=M([[1,0,-1,0],[0,1,0,-1]])
null(A,G,'2.5 equations from generators');eq(G.rank(),2,'2.5 generator rank in R4');eq(A.rank(),2,'2.5 independent equations in R4')
eq(M([[1,1],[1,-1]]).inv()*M([3,1]),M([2,1]),'2.5 E01 coordinates')
null(M([[1,1,1],[0,1,-1]]),M([-2,1,1]),'2.5 E02 direction')
eq(M([[1,0],[2,1],[0,1]])*M([2,1]),M([2,5,1]),'2.5 E03 membership')
null(M([[1,0,-1],[1,1,0]]),M([1,-1,1]),'2.6 E01 intersection')
eq(M([[1,0,0],[0,1,0],[1,0,1]]).rank(),3,'2.6 E01 sum rank')
eq(M([[1,c],[0,1]])*M([x-c*y,y]),M([x,y]),'2.6 all complements decomposition')
eq(M([[1,1],[1,-1]]).inv()*M([x,y]),M([(x+y)/2,(x-y)/2]),'2.6 E04 direct sum decomposition')
# Dimension examples by the rank formula independently evaluated for concrete matrices.
for n,Uidx,Widx,expected,label in [(3,[0,1],[1,2],1,'2.7 two planes'),(5,[0,1,2,3],[2,3,4],2,'2.7 lower bound sharp'),(5,[0,1,2],[2,3,4],1,'2.7 E03 dim1'),(5,[0,1,2],[1,2,3],2,'2.7 E03 dim2'),(5,[0,1,2],[0,1,2],3,'2.7 E03 dim3')]:
 E=s.eye(n);U=E[:,Uidx];W=E[:,Widx];eq(U.rank()+W.rank()-U.row_join(W).rank(),expected,label)
F=M([[1,2,-1],[0,1,1]])
eq(F*M([1,0,1]),M([0,1]),'3.1 rectangular action');eq(M([[1,-1],[1,0]])*M([[1,1],[0,1]]),M([[1,0],[1,1]]),'3.1 assigned base images')
null(F,M([3,-1,1]),'3.2 kernel rectangular');eq(F.rank(),2,'3.2 image rank');eq(F[:,[0,1]].det(),1,'3.2 independent image columns')
D=M([[0,1,0,0],[0,0,2,0],[0,0,0,3]]);eq(D.rank(),3,'3.2 derivative rank')
null(M([[1,1,0],[0,1,1]]),M([-1,1,-1]),'3.2 E01 kernel')
null(M([[1,1,1]]),M([[-1,-1],[1,0],[0,1]]),'3.2 E02 evaluation kernel')
fa=M([[1,a],[a,1]]);eq(fa.det(),1-a*a,'3.3 parameter determinant');eq(fa.inv(),M([[1,-a],[-a,1]])/(1-a*a),'3.3 inverse formula')
null(fa.subs(a,1),M([-1,1]),'3.3 a1 kernel');null(fa.subs(a,-1),M([1,1]),'3.3 a-1 kernel')
T=M([[1,1,0],[0,1,1],[1,0,-1]]);eq(T.rank(),2,'3.3 E01 rank');null(T,M([-1,1,-1]),'3.3 E01 kernel')
Ev=M([[1,-1,1],[1,0,0],[1,1,1]])
eq(Ev.inv()*M([x,y,z]),M([y,(z-x)/2,(z+x)/2-y]),'3.4 interpolation coefficients')
eq(M([[1,1],[1,-1]]).inv(),M([[1,1],[1,-1]])/2,'3.4 explicit inverse')
# Quotients: representative reductions are checked against the subspace generators.
eq(M([a,b,c])-M([a-c,b-c,0]),c*M([1,1,1]),'2.9 quotient coordinates')
eq(M([[1,1,0],[0,1,1]])*M([a,0,b]),M([a,b]),'2.9 induced map surjectivity')
# Matrix representation and independent basis transformations.
A=M([[1,2],[3,-1]]);B=M([[1,1],[1,-1]]);C=M([[1,1],[0,1]])
eq(C.inv()*A*B,M([[1,-5],[2,4]]),'3.5 two bases representation')
eq(B.inv()*M([3,1]),M([2,1]),'3.5 input coordinates');eq(M([[1,-5],[2,4]])*M([2,1]),M([-3,8]),'3.5 output coordinates');eq(C*M([-3,8]),A*M([3,1]),'3.5 output reconstruction')
D=M([[0,1,0],[0,0,2]]);J=M([[0,0],[1,0],[0,R(1,2)]])
eq(D*J,s.eye(2),'3.5 derivative primitive DJ');eq(J*D,s.diag(0,1,1),'3.5 derivative primitive JD')
F=M([[1,0],[0,1],[1,1]]);G=M([[1,0,1],[0,1,-1]])
eq(G*F,M([[2,1],[-1,0]]),'3.5 E04 composition')
eq(B.inv()*s.diag(2,3)*B,M([[5,-1],[-1,5]])/2,'3.6 conjugation')
P=M([[1,0],[1,1]]);eq(P.inv()*s.diag(1,2)*P,M([[1,0],[1,2]]),'3.6 E02 changed endomorphism')
Rot=M([[0,-1],[1,0]]);eq(Rot**2,-s.eye(2),'3.6 nonsimilarity square')
A=M([[1,2,0],[0,3,1],[2,0,1]]);eq(A.det(),7,'3.7 determinant example')
A=M([[2,1],[3,2]]);eq(A.adjugate(),M([[2,-1],[-3,2]]),'3.7 adjugate');eq(A.inv(),M([[2,-1],[-3,2]]),'3.7 cofactor inverse')
eq(M([[1,1],[1,t]]).det(),t-1,'3.7 parameter determinant');eq(M([[1,1],[1,t]]).inv(),M([[t,-1],[-1,1]])/(t-1),'3.7 parameter inverse')
eq(B.inv().T*B.T,s.eye(2),'3.8 dual basis change evaluation')
eq(B.T*M([2,3]),M([5,-1]),'3.8 functional coordinates')
eq(M([[1,2],[0,1]]).T*M([3,-1]),M([3,5]),'3.8 transpose pullback')
# Spectral and Jordan computations, using exact symbolic arithmetic.
A=M([[2,1],[0,3]]);eq(A.charpoly(t).as_expr(),(t-2)*(t-3),'4.1 characteristic triangular')
null(A-2*s.eye(2),M([1,0]),'4.1 eigenvector 2');null(A-3*s.eye(2),M([1,1]),'4.1 eigenvector 3')
eq(Rot.charpoly(t).as_expr(),t*t+1,'4.1 rotation characteristic');null(Rot-s.I*s.eye(2),M([1,-s.I]),'4.1 complex vector')
eq(M([[0,1],[2,0]]).charpoly(t).as_expr(),t*t-2,'4.1 rational field example')
eq(M([[1,2],[3,4]]).charpoly(t).as_expr(),t*t-5*t-2,'4.1 E03 characteristic')
A=M([[1,0,0],[0,2,1],[0,0,2]]);eq(A.charpoly(t).as_expr(),(t-1)*(t-2)**2,'4.2 characteristic multiplicities');eq(3-(A-2*s.eye(3)).rank(),1,'4.2 geometric multiplicity')
A=M([[3,1,0],[0,3,0],[0,0,4]]);eq(3-(A-3*s.eye(3)).rank(),1,'4.2 E01 g3');eq(3-(A-4*s.eye(3)).rank(),1,'4.2 E01 g4')
A=M([[2,1],[0,3]]);P=M([[1,1],[0,1]])
eq(A*P,P*s.diag(2,3),'4.3 diagonalization relation AP=PD');eq(P.inv(),M([[1,-1],[0,1]]),'4.3 diagonalizer inverse')
A=M([[2,1],[1,2]]);P=M([[1,1],[-1,1]])
eq(P.inv()*A*P,s.diag(1,3),'4.3 symmetric example diagonalization')
for n in [0,1,2,5,9]:eq(A**n,M([[1+3**n,3**n-1],[3**n-1,1+3**n]])/2,f'4.3 power k={n}')
A=M([[1,1],[0,2]])
for n in [0,1,3,7]:eq(A**n,M([[1,2**n-1],[0,2**n]]),f'4.3 E01 power k={n}')
P=M([[1,1],[-1,0]])
for lam,A in [(2,M([[3,1],[-1,1]])),(1,M([[2,1],[-1,0]]))]:
 N=A-lam*s.eye(2);J=M([[lam,1],[0,lam]])
 eq(N**2,s.zeros(2),f'4.4 nilpotent part lambda={lam}');eq(A*P,P*J,f'4.4 AP=PJ lambda={lam}');eq(P.inv(),M([[0,-1],[1,1]]),f'4.4 inverse P lambda={lam}')
N=s.diag(M([[0,1,0],[0,0,1],[0,0,0]]),M([[0,1],[0,0]]),M([[0]]))
eq([6-(N**i).rank() for i in range(1,5)],[3,5,6,6],'4.4 block dimension data');eq(N.rank(),3,'4.4 nilpotent rank')
N31=s.diag(M([[0,1,0],[0,0,1],[0,0,0]]),M([[0]]));N22=s.diag(M([[0,1],[0,0]]),M([[0,1],[0,0]]))
eq([4-(N31**i).rank() for i in range(1,4)],[2,3,4],'4.4 partition 3,1');eq([4-(N22**i).rank() for i in range(1,4)],[2,4,4],'4.4 partition 2,2')
A=M([[2,1],[0,3]]);eq(A*A-5*A+6*s.eye(2),s.zeros(2),'4.5 CH example');eq(A.inv(),(5*s.eye(2)-A)/6,'4.5 inverse from characteristic')
N=M([[0,1,0],[0,0,1],[0,0,0]]);eq(N**3,s.zeros(3),'4.5 nilpotent index');eq(M.hstack(s.eye(3).reshape(9,1),N.reshape(9,1),(N**2).reshape(9,1)).rank(),3,'4.5 powers independent before annihilation')
# Functional calculus checked against direct powers and SymPy exponential.
A=M([[2,1],[0,2]])
for n in [0,1,2,4,9]:
 predicted=s.eye(2) if n==0 else M([[2**n,n*2**(n-1)],[0,2**n]])
 eq(A**n,predicted,f'4.6 Jordan powers k={n}')
eq((t*A).exp(),s.exp(2*t)*M([[1,t],[0,1]]),'4.6 Jordan exponential')
eq((t*N).exp(),M([[1,t,t*t/2],[0,1,t],[0,0,1]]),'4.6 nilpotent exponential')
A=M([[R(1,2),1],[0,R(1,2)]])
for n in [0,1,3,8]:
 predicted=s.eye(2) if n==0 else M([[R(1,2)**n,n*R(1,2)**(n-1)],[0,R(1,2)**n]])
 eq(A**n,predicted,f'4.6 stable Jordan k={n}')
phi=(1+s.sqrt(5))/2;psi=(1-s.sqrt(5))/2
for n in [0,1,2,3,5,10]:eq((phi**n-psi**n)/s.sqrt(5),s.fibonacci(n),f'4.6 Fibonacci k={n}')
A=s.diag(M([[1,1],[0,1]]),M([[2]]));H=s.E*s.eye(3)+s.E*(A-s.eye(3))+(s.exp(2)-2*s.E)*(A-s.eye(3))**2
eq(A.exp(),H,'4.6 Hermite exponential interpolation')
A=M([[3,-2],[1,0]])
for n in [0,1,2,5]:eq(A**n*M([1,0]),M([2**(n+1)-1,2**n-1]),f'4.6 recurrence k={n}')
P=M([[1,1],[1,0]]);A=P*s.diag(2,R(1,2))*P.inv();eq(A,M([[R(1,2),R(3,2)],[0,2]]),'4.6 stable initial subspace matrix')
for n in [0,1,2,6]:eq(A**n*M([x,y]),2**n*y*M([1,1])+R(1,2)**n*(x-y)*M([1,0]),f'4.6 E07 orbit k={n}')

failed=[check for check in checks if not check['passed']]
print(json.dumps({'exact_checks':len(checks),'failed':failed,'passed':not failed},ensure_ascii=False,indent=2))
raise SystemExit(bool(failed))
