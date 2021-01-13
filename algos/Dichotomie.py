from .Equa_Solver import *

from .basic_functions import *


from ast import literal_eval

"""
    res_equa_dct(f,a,b)

    Cette fonction résout l'equation f(x)=0
    pour une fonction f monotonne (croissante ou décroissante)
    sur un intervale [a,b] le pseudo code de cette fonction
    est disponible sur le ReadMe du dépot
    
    # Méthode Dichotomie 

    Début
    debut <- a
    fin   <- b

    TantQue ( fin-debut > err )
    {
        millieu = (debut + fin ) / 2

        Si  ( f(millieu) >  0 )
        {
            fin <- millieu
        } 
        Sinon 
        {
            debut <- millieu
        }
    }
    retourner (millieu) 
    Fin
    ```
    
"""

class Dichotomie(Equa_Solver):

    def solve(self):
        # Données en parametres
        a , b = self.a , self.b
        err=self.err
        try:
            f = lambda x: eval(str(self.f))
        except (TypeError,SyntaxError):
            return
        x_list=[]

        print(f" Fonction   : {self.f}")
        print(f" Intervalle : [{a},{b}]")
        print(f" Erreur     : {err} \n")


        if( f(a)*f(b) > 0):
            raise SolverException(" f(a) et f(b) doivent etre de signe différent !")

        else:
            debut = a
            fin = b
            n=1

            while (fin - debut > err):
                millieu = (debut + fin) / 2
                x_list.append(millieu)
                print(f"Found solution after {n} iterations : {millieu} ")
                n+=1
                if (f(debut) * f(millieu) < 0):
                    fin = millieu
                else:
                    debut = millieu

            print(f" Solution approchée de f(x) = 0 est : {millieu}\n")
            return x_list


