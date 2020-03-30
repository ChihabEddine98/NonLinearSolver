from algos.Dichotomie import *
from algos.Equa_Solver import *

class DichotomieTester:

    def test1(self):
        print("-----------------------------------")
        print("|        Méthode Dichotomie        |")
        print("-----------------------------------")

        f="x**2-math.cos(x)"
        equa=Equa_Solver(f=f,a=0,b=1,err=1e-8)
        return Dichotomie.solve(equa)

    def test2(self):

        print("-----------------------------------")
        print("|        Méthode Dichotomie        |")
        print("-----------------------------------")

        f="x**3 - x**2 - 1"
        equa=Equa_Solver(f=f,a=1,b=2,err=1e-8)
        return Dichotomie.solve(equa)

    def test3(self):
        print("-----------------------------------")
        print("|        Méthode Dichotomie        |")
        print("-----------------------------------")
        f="math.cos(2*x)**2 - x**2"
        equa=Equa_Solver(f=f,a=0,b=2,err=1e-8)
        return Dichotomie.solve(equa)

    def test4(self):
        print("-----------------------------------")
        print("|        Méthode Dichotomie        |")
        print("-----------------------------------")
        f = "math.cos(x)"
        equa=Equa_Solver(f=f,a=0,b=2,err=1e-8)
        return Dichotomie.solve(equa)

    def test5(self):
        print("-----------------------------------")
        print("|        Méthode Dichotomie        |")
        print("-----------------------------------")
        f="x**3 - 4*x + 1"
        equa=Equa_Solver(f=f,a=0,b=1,err=1e-8)
        return Dichotomie.solve(equa)



    def test(self):
        self.test1()
        self.test2()
        self.test3()