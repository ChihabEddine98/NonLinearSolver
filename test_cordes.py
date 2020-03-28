import cordes 
import math

def test1():
    f="x**2-cos(x)"
    print(cordes.res_equa_cordes(f,0.0,1.0,1e-8))

def test2():
    f="x**3 - x**2 - 1"
    print(cordes.res_equa_cordes(f,1.0,2,1e-8))

def test3(): 
    f="cos(2*x)**2 - x**2"
    print(cordes.res_equa_cordes(f,0.0,1))

def test4():
    f="cos(x)"
    print(cordes.res_equa_cordes(f,0.0,3.0))

def test5():
    f="x**3 - 4*x + 1"
    print(cordes.res_equa_cordes(f,1.0,2.0))


if __name__=='__main__':
    print("-----------------------------------")
    print("|        Méthode Cordes            |")
    print("-----------------------------------\n\n",)
    test1()
    test2()
    test3()
    test4()
    test5()
    