from .Equa_Solver import *
import numpy as np
import math
from .basic_functions import *


class Cordes(Equa_Solver):

    def solve(self):

        f=self.f
        a,b =self.a,self.b
        max_iter=self.max_iter
        epsilon=self.err
        x_list=[]

        fx = lambda x: eval(str(f))
        print("\n\nfunction f : ", f, " dans l'intervalle [", a, ",", b, "] \n", "--------------------------------")


        for n in range(0, max_iter):
            self.affiche_info(n, b, fx(b))
            x_list.append(b)
            if (abs(a - b) < epsilon):
                print('Found solution after', n, 'iterations.')
                return x_list

            z = (a * fx(b) - b * fx(a)) / (fx(b) - fx(a))
            a, b = b, z

        print('Exceeded maximum iterations =', max_iter, '.No solution found.')
        return None

