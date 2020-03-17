import math
from sympy import *

def affiche_infos(n,xn,fxn):
    print("iteration : ",n,)
    print("xn : ",xn,)
    print("f(xn) : ",fxn,)
    print("tol : ",abs(fxn-0),"\n")



def res_equa_newton(f,Df,x0,epsilon,max_iter):
    fx=lambda x: eval(str(f))
    dfx=lambda x: eval(str(Df))
    print("\n\nfunction f : ",f,"\n","Derivative f' : ",Df,"\n","--------------------------------")

    xn = x0
    for n in range(0,max_iter):
        fxn = fx(xn)
        affiche_infos(n,xn,fxn)
     
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
    print("\n\nfunction f : ",f,"\n","Derivative f' : ",diff(f),"\n","--------------------------------")
    
    xn = x0
   
    for n in range(0,max_iter):
        fxn = fx(xn)
        affiche_infos(n,xn,fxn)
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
    

