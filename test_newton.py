import newton 
import math

def test1():
    f="x**2-cos(x)"
    Df="2*x+math.sin(x)"
    print(newton.res_equa_newton(f,Df,math.pi/4,1e-8,10))

def test2():
    f="x**3 - x**2 - 1"
    Df="3*x**2-2*x"
    print(newton.res_equa_newton(f,Df,0.75,1e-8,10))

def test3(): 
    f="cos(2*x)**2 - x**2"
    print(newton.res_equa_newton_withoutDf(f,0.75,1e-10,10))

if __name__=='__main__':
    print("-----------------------------------")
    print("|        Méthode Newton        |")
    print("-----------------------------------\n\n",)
    test1()
    test2()
    test3()
    print("on remarque que la puissance de l'erreur double à chaque itération,donc la méthode est d'ordre 2,\n La convergence est quadratique.")
