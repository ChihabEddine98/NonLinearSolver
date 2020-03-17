import dichotomie as dct
import math

class Tests_Dico():

    # f1(x) = x^3+x-1
    def affiche_f1(self):
        return "f(x) = x^3+x-1 "
    def f1(self,x):
        return x**3+x-1 

    # f2(x) = x-exp(sin(x))    
    def affiche_f2(self):
        return "f(x) = x-exp(sin(x)) "
    def f2(self,x):
        return x-math.exp(math.sin(x))

    # f3(x) = cos(x)-x³    
    def affiche_f3(self):
        return "f(x) = cos(x)-x³ "
    def f3(self,x):
        return math.cos(x)-pow(x,3)

def test(f,f_str,interval,err):
    tst_dico=Tests_Dico()
    print("-----------------------------------")
    print("|        Méthode Dichotomie        |")
    print("-----------------------------------")
    print(f" Fonction   : {f_str}")
    print(f" Intervalle : {interval}")
    print(f" Erreur     : {err} \n")
    sol=dct.res_equa_dct(f,interval[0],interval[1],err)
    print(f" Solution approchée de f(x) = 0 est : {sol}\n")

def test0():
    tst_dico=Tests_Dico()
    test(tst_dico.f1,tst_dico.affiche_f1(),[0,1],10**-8)

def test4():
    tst_dico=Tests_Dico()
    test(tst_dico.f2,tst_dico.affiche_f2(),[2,3],10**-8)

def test5():
    tst_dico=Tests_Dico()
    test(tst_dico.f3,tst_dico.affiche_f3(),[0,1],10**-8)
