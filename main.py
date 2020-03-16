import dichotomie as dct
from tests import *



if __name__ == '__main__':
    print("-----------------------------------")
    print("|        Méthode Dichotomie        |")
    print("-----------------------------------")
    f1_str=Tests_Dico.affiche_f1()
    print(f" Fonction   : {f1_str}")
    interval =[0,1]
    print(f" Intervalle : {interval}")
    err=10**-8
    print(f" Erreur     : {err} \n")
    sol=dct.res_equa_dct(Tests_Dico.f1,interval[0],interval[1],err)
    print(f" Solution approchée de f1(x) = 0 est : {sol}\n")
    
    