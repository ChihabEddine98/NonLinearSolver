import dichotomie as dct

class Tests_Dico():

    # f1(x) = x^3+x-1
    def affiche_f1(self):
        return "f1(x) = x^3+x-1 "
    def f1(self,x):
        return x**3+x-1 

def test(f,f_str,interval,err):
    tst_dico=Tests_Dico()
    print("-----------------------------------")
    print("|        Méthode Dichotomie        |")
    print("-----------------------------------")
    print(f" Fonction   : {f_str}")
    print(f" Intervalle : {interval}")
    print(f" Erreur     : {err} \n")
    sol=dct.res_equa_dct(f,interval[0],interval[1],err)
    print(f" Solution approchée de f1(x) = 0 est : {sol}\n")

def test1():
    tst_dico=Tests_Dico()
    test(tst_dico.f1,tst_dico.affiche_f1(),[0,1],10**-8)
