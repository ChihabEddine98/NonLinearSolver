import dichotomie as dct
from test_dicho import *
from test_newton import *



if __name__ == '__main__':
    # Tests Méthode Dichotomie :
    test0()



    #Tests Methode Newton :
    print("-----------------------------------")
    print("|        Méthode Newton        |")
    print("-----------------------------------\n\n",)
    test1()
    test2()
    test3()
    print("on remarque que la puissance de l'erreur double à chaque itération,donc la méthode est d'ordre 2,\n La convergence est quadratique.")
    
    