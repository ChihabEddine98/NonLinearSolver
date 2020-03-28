from math import *

def res_equa_false_pos(f, a, b, tol=1e-10):
    fx=lambda x: eval(str(f))
    print("\n\nfunction f : ", f," dans l'intervalle [",a,",",b,"] \n", "--------------------------------")

    if fx(a)*fx(b) > 0:
        raise ValueError("f(a) et f(b) doivent avoir un signe différent")
    n = 0
    while abs(b-a) > 2*tol:
        n += 1
        c = (a*fx(b)-b*fx(a))/(fx(b)-fx(a))
        if fx(c-tol) * fx(c+tol) <= 0:
            print('Found solution after',n,'iterations.')
            return c
        if fx(a)*fx(c) > 0:
            a = c
        else:
            b = c
    print('Found solution after',n,'iterations.')
    return (a+b)/2


