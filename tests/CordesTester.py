from algos.Cordes import *
from algos.Equa_Solver import *
from convergence_rate import *




class CordesTester:

    def test1(self):
        print("-----------------------------------")
        print("|        Méthode Cordes            |")
        print("-----------------------------------", )
        f = "x**2-cos(x)"
        equa=Equa_Solver(f=f,err=1e-8,a=0.0,b=1.0,max_iter=10)
        x_list=Cordes.solve(equa)

        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)

    def test2(self):
        print("-----------------------------------")
        print("|        Méthode Cordes            |")
        print("-----------------------------------", )
        f = "x**3 - x**2 - 1"
        equa=Equa_Solver(f=f,err=1e-8,a=1.0,b=2,max_iter=10)
        x_list=Cordes.solve(equa)

        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)

    def test3(self):
        print("-----------------------------------")
        print("|        Méthode Cordes            |")
        print("-----------------------------------", )
        f = "cos(2*x)**2 - x**2"
        equa=Equa_Solver(f=f,a=0.0,b=1)
        x_list=Cordes.solve(equa)

        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)

    def test4(self):
        print("-----------------------------------")
        print("|        Méthode Cordes            |")
        print("-----------------------------------", )
        f = "cos(x)"
        equa=Equa_Solver(f=f,a=0.0,b=3.0)
        x_list=Cordes.solve(equa)
        
        x_final=x_list[-1]
        x_list.pop()
        x_list.pop()

        print_rates(x_list,x_final)

    def test5(self):
        print("-----------------------------------")
        print("|        Méthode Cordes            |")
        print("-----------------------------------", )
        f = "x**3 - 4*x + 1"
        equa=Equa_Solver(f=f,a=-3.0,b=-2.0)
        x_list=Cordes.solve(equa)

        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)

    def test6(self):
        print("-----------------------------------")
        print("|        Méthode Cordes            |")
        print("-----------------------------------", )
        f = "x-exp(-x)"
        equa=Equa_Solver(f=f,a=0.0,b=1.0)
        x_list=Cordes.solve(equa)

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
