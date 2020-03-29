from algos.Newton import *
from algos.Equa_Solver import *

import math



class NewtonTester:

    def test1(self):
        f="x**2-math.cos(x)"
        Df="2*x+math.sin(x)"
        equa=Newton(f=f,df=Df,err=1e-8,x0=math.pi/4,max_iter=10)
        print(Newton.solve(equa))

    def test2(self):
        f="x**3 - x**2 - 1"
        Df="3*x**2-2*x"
        equa=Newton(f=f,df=Df,err=1e-8,x0=0.75,max_iter=10)
        print(Newton.solve(equa))

    def test3(self):
        f="cos(2*x)**2 - x**2"
        equa=Newton(f=f,err=1e-10,x0=0.75,max_iter=10)
        print(Newton.solve(equa))

    def test4(self):
        f="cos(x)"
        equa=Newton(f=f,err=1e-10,x0=1.0,max_iter=10)
        print(Newton.solve(equa))

    def test5(self):
        f="x**3 - 4*x + 1"
        equa=Newton(f=f,err=1e-10,x0=-3,max_iter=10)
        print(Newton.solve(equa))

    def test(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
        print(
            "\n \n on remarque que la puissance de l'erreur double à chaque itération,donc la méthode est d'ordre 2,\n La convergence est quadratique.")

