from algos.Newton import *
from algos.Equa_Solver import *
from convergence_rate import *

import math


class NewtonTester:

    def test1(self):
        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------", )
        f = "x**2-cos(x)"
        Df = "2*x+sin(x)"
        equa = Newton(f=f, df=Df, err=1e-8, x0=math.pi/4, max_iter=10)
        x_list = Newton.solve(equa)

        print_rate(x_list)

    def test2(self):
        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------", )

        f = "x**3 - x**2 - 1"
        Df = "3*x**2-2*x"
        equa = Newton(f=f, df=Df, err=1e-8, x0=0.75, max_iter=10)
        x_list = Newton.solve(equa)

        print_rate(x_list)

    def test3(self):
        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------", )
        f = "cos(2*x)**2 - x**2"
        equa = Newton(f=f, err=1e-10, x0=0.75, max_iter=10)
        x_list = Newton.solve(equa)
        print_rate(x_list)

    def test4(self):
        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------", )
        f = "cos(x)"
        equa = Newton(f=f, err=1e-10, x0=1.0, max_iter=10)
        x_list = Newton.solve(equa)

        print_rate(x_list)

    def test5(self):
        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------", )
        f = "x**3 - 4*x + 1"
        equa = Newton(f=f, err=1e-10, x0=-3, max_iter=10)
        x_list = Newton.solve(equa)

        print_rate(x_list)

    def test(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
