

class SolverException(Exception):
    def __init__(self,message):
        super().__init__(message)

class Equa_Solver :

    def __init__(self,f,err=1e-10,x0=0,a=0,b=0,df=None,max_iter=40):
        self.f=f
        self.err=err
        self.x0=x0
        self.a,self.b=a,b
        self.df=df
        self.max_iter=max_iter

    def affiche_info(self,n,xn,fxn):
        print("iteration : ",n,)
        print("xn : ",xn,)
        print("f(xn) : ",fxn,)
        print("tol : ",abs(fxn-0),"\n")
