import math
from sympy import *

def res_equa_newton(f,Df,x0,epsilon,max_iter):
    fx=lambda x: eval(str(f))
    dfx=lambda x: eval(str(Df))

    xn = x0
    for n in range(0,max_iter):
        fxn = fx(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = dfx(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

def res_equa_newton_withoutDf(f,x0,epsilon,max_iter):
    x=Symbol('x')
    fx=lambda x: eval(str(f))
    dfx=lambda x: eval(str(diff(f)))
    
    xn = x0
   
    for n in range(0,max_iter):
        fxn = fx(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = dfx(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None
    
if __name__=='__main__':
    print("-----------------------------------")
    print("|        Méthode Newton        |")
    print("-----------------------------------\n\n",)
    x=Symbol('x')
    f1= x**3 - x**2 - 1
    df1= 3*x**2-2*x

    print("f(x)=",f1)
    print("f'(x)=",df1)
    print(res_equa_newton(f1,df1,0.75,1e-10,10),"\n")

    f2=cos(2*x)**2 - x**2
    print("f(x)=",f2)
    print(res_equa_newton_withoutDf(f2,0.75,1e-10,10))
    

    

