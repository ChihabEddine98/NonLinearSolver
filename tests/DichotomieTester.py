from algos.Dichotomie import *
from algos.Equa_Solver import *

class DichotomieTester:

    def test1(self):
        f="x**3+x-1"
        equa=Equa_Solver(f=f,a=0,b=1,err=1e-8)
        return Dichotomie.solve(equa)

    def test2(self):

        f="x-math.exp(math.sin(x))"
        equa=Equa_Solver(f=f,a=2,b=3,err=1e-8)
        return Dichotomie.solve(equa)

    def test3(self):
        f="math.cos(x)-x**3"
        equa=Equa_Solver(f=f,a=0,b=1,err=1e-8)
        return Dichotomie.solve(equa)

    def test(self):
        self.test1()
        self.test2()
        self.test3()