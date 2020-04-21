from .Equa_Solver import *
import math

class Cordes(Equa_Solver):

    def solve(self):

        f=self.f
        a,b =self.a,self.b
        max_iter=self.max_iter
        epsilon=self.err

        fx = lambda x: eval(str(f))
        print("\n\nfunction f : ", f, " dans l'intervalle [", a, ",", b, "] \n", "--------------------------------")

        res=[]
        for n in range(0, max_iter):
            self.affiche_info(n, b, fx(b))
            res.append(b)
            if (abs(a - b) < epsilon):
                print('Found solution after', n, 'iterations.')
                return res

            z = (a * fx(b) - b * fx(a)) / (fx(b) - fx(a))
            a, b = b, z

        print('Exceeded maximum iterations =', max_iter, '.No solution found.')
        return None

