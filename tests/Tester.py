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

        print('--------------------------------------- Test 01--------------------------------------------')
        dichotomie.test1(dichotomie())
        newton.test1(newton())
        cordes.test1(cordes())
        falsePos.test1(falsePos())

        print('--------------------------------- -------------------------------------------------- Test 02 ------------------------------------ ----------------------------------------------------')
        dichotomie.test2(dichotomie())
        newton.test2(newton())
        cordes.test2(cordes())
        falsePos.test2(falsePos())

        print('---------v------------------------ ------------------------------------------------- Test 03 -------------------------------- --------------------------------------------------------')
        dichotomie.test3(dichotomie())
        newton.test3(newton())
        cordes.test3(cordes())
        falsePos.test3(falsePos())

        print('--------------------------------- -------------------------------------------------- Test 04 ------------------------------ ----------------------------------------------------------')
        dichotomie.test4(dichotomie())
        newton.test4(newton())
        cordes.test4(cordes())
        falsePos.test4(falsePos())

        print('---------------------------------- ------------------------------------------------- Test 05 ------------------------------- ---------------------------------------------------------')
        dichotomie.test5(dichotomie())
        newton.test5(newton())
        cordes.test5(cordes())
        falsePos.test5(falsePos())




        







