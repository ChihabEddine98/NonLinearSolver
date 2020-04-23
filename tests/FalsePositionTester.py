from algos.FalsePosition import *
from algos.Equa_Solver import *
from convergence_rate import *



class FalsePositionTester :

    def test1(self):
        print("-----------------------------------")
        print("|        Méthode Fausse position   |")
        print("-----------------------------------", )
        f = "x**2-math.cos(x)"
        equa=Equa_Solver(f=f,err=1e-8,a=0.0,b=1.0)
        x_list=FalsePosition.solve(equa)

        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)

    def test2(self):
        print("-----------------------------------")
        print("|        Méthode Fausse position   |")
        print("-----------------------------------", )
        f = "x**3 - x**2 - 1"
        equa=Equa_Solver(f=f,err=1e-8,a=1.0,b=2.0)
        x_list=FalsePosition.solve(equa)

        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)

    def test3(self):
        print("-----------------------------------")
        print("|        Méthode Fausse position   |")
        print("-----------------------------------", )
        f = "math.cos(2*x)**2 - x**2"
        equa=Equa_Solver(f=f,a=0.0,b=1)
        x_list=FalsePosition.solve(equa)

        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)

    def test4(self):
        print("-----------------------------------")
        print("|        Méthode Fausse position   |")
        print("-----------------------------------", )
        f = "math.cos(x)"
        equa=Equa_Solver(f=f,a=0.0,b=3.0)
        x_list=FalsePosition.solve(equa)

        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)

    def test5(self):
        print("-----------------------------------")
        print("|        Méthode Fausse position   |")
        print("-----------------------------------", )
        f = "x**3 - 4*x + 1"
        equa=Equa_Solver(f=f,a=1.0,b=2.0)
        x_list=FalsePosition.solve(equa)
        print(x_list)
        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)

    def test6(self):
        print("-----------------------------------")
        print("|        Méthode Fausse position   |")
        print("-----------------------------------", )
        f = "x-math.exp(-x)"
        equa=Equa_Solver(f=f,a=0.0,b=1.0)
        x_list=FalsePosition.solve(equa)

        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)

    def test(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()
        self.test6()