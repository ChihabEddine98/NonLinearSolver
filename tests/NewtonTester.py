from algos.Newton import *
from algos.Equa_Solver import *

import math
from math import log

def rate(x_list, x_final):
    e = [abs(x_ - x_final) for x_ in x_list]
    print (e)
    q = [(log(e[n+1]/e[n]))/(log(e[n]/e[n-1])) for n in range(1, len(e)-1, 1)]
    return q

def print_rates( x_list, x_final):
    q = ['%.2f' % q_ for q_ in rate(x_list, x_final)]
    print ("Convergence rate : ")
    for q_ in q:
        print(q_)
    print()

class NewtonTester:

    def test1(self):
        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------", )
        f="x**2-cos(x)"
        Df="2*x+sin(x)"
        equa=Newton(f=f,df=Df,err=1e-8,x0=math.pi/4,max_iter=10)
        x_list=Newton.solve(equa)

        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)
    

    def test2(self):
        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------", )

        f="x**3 - x**2 - 1"
        Df="3*x**2-2*x"
        equa=Newton(f=f,df=Df,err=1e-8,x0=0.75,max_iter=10)
        x_list=Newton.solve(equa)
        
        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)
    
    def test3(self):
        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------", )
        f="cos(2*x)**2 - x**2"
        equa=Newton(f=f,err=1e-10,x0=0.75,max_iter=10)
        x_list=Newton.solve(equa)
        
        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)
    

    def test4(self):
        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------", )
        f="cos(x)"
        equa=Newton(f=f,err=1e-10,x0=1.0,max_iter=10)
        x_list=Newton.solve(equa)
        
        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)
    

    def test5(self):
        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------", )
        f="x**3 - 4*x + 1"
        equa=Newton(f=f,err=1e-10,x0=-3,max_iter=10)
        x_list=Newton.solve(equa)
        
        x_final=x_list[-1]
        x_list.pop()

        print_rates(x_list,x_final)
    


    def test(self):
        self.test1()
        self.test2()
        self.test3()
        self.test4()
        self.test5()

