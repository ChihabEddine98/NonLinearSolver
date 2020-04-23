from .Equa_Solver import *
import math


class FalsePosition(Equa_Solver):

    def solve(self):
        f=self.f
        a,b=self.a,self.b
        tol=self.err
        x_list=[]
        fx = lambda x: eval(str(f))
        print("\n\nfunction f : ", f, " dans l'intervalle [", a, ",", b, "] \n", "--------------------------------")

        if fx(a) * fx(b) > 0:
            raise SolverException(" f(a) et f(b) doivent etre de signe différent !")

        n = 0
        while abs(b - a) > 2 * tol:
            n += 1
            c = (a * fx(b) - b * fx(a)) / (fx(b) - fx(a))
            x_list.append(c)

            if fx(c - tol) * fx(c + tol) <= 0:
                print('Found solution after', n, 'iterations.')
                return x_list
            if fx(a) * fx(c) > 0:
                a = c
            else:
                b = c
            
        print('Found solution after', n, 'iterations.')
        x_list.append((a+b)/2)
        return x_list