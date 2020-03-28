import falsePos
import math

def test1():
    f="x**2-cos(x)"
    print(falsePos.res_equa_false_pos(f,0.0,1.0,1e-8))

def test2():
    f="x**3 - x**2 - 1"
    print(falsePos.res_equa_false_pos(f,1.0,2,1e-8))

def test3(): 
    f="cos(2*x)**2 - x**2"
    print(falsePos.res_equa_false_pos(f,0.0,1))

def test4():
    f="cos(x)"
    print(falsePos.res_equa_false_pos(f,0.0,3.0))

def test5():
    f="x**3 - 4*x + 1"
    print(falsePos.res_equa_false_pos(f,1.0,2.0))

def test6():
    f="x-exp(-x)"
    print(falsePos.res_equa_false_pos(f,0.0,1.0))



if __name__=='__main__':
    print("-----------------------------------")
    print("|        Méthode Fausse position   |")
    print("-----------------------------------\n\n",)
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()