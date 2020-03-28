from math import *
import newton

def res_equa_cordes(f, a, b, epsilon=1e-10, max_iter=40):
    fx=lambda x: eval(str(f))
    print("\n\nfunction f : ", f," dans l'intervalle [",a,",",b,"] \n", "--------------------------------")

    for n in range(0,max_iter):
        newton.affiche_infos(n,b,fx(b))

        if( abs(a-b) < epsilon):
            print('Found solution after',n,'iterations.')
            return b

        z = ( a*fx(b) - b*fx(a) ) / ( fx(b) - fx(a) )
        a,b = b,z

    print('Exceeded maximum iterations =',max_iter,'.No solution found.')
    return None


