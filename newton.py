def res_equa_newton(f,df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found.')
    return None

if __name__=='__main__':
    f= lambda x: x**3 - x**2 - 1
    Df= lambda x: 3*x**2-2*x
    print(res_equa_newton(f,Df,1,1e-10,10))


