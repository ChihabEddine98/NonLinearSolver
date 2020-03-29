from .DichotomieTester import DichotomieTester as dichotomie
from .NewtonTester import NewtonTester as newton
from .CordesTester import CordesTester as cordes
from .FalsePositionTester import FalsePositionTester as falsePos



class Tester:

    # def __init__(self,f,err,x0=0,a=0,b=0,df=None,max_iter=None):
    #     self.f=f
    #     self.err=err
    #     self.x0=x0
    #     self.a,self.b=a,b
    #     self.df=df
    #     self.max_iter=max_iter


    def test(self):

        print('--------------- Test des méthodes --------------------\n')
        print("-----------------------------------")
        print("|        Méthode Dichotomie        |")
        print("-----------------------------------")

        dichotomie.test(dichotomie())

        print("-----------------------------------")
        print("|        Méthode Newton            |")
        print("-----------------------------------\n\n", )

        newton.test(newton())

        print("-----------------------------------")
        print("|        Méthode Cordes            |")
        print("-----------------------------------\n\n", )

        cordes.test(cordes())

        print("-----------------------------------")
        print("|        Méthode Fausse position   |")
        print("-----------------------------------\n\n", )

        falsePos.test(falsePos())



