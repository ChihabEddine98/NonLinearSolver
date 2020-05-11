from math import log

def rate(x_list, x_final):
    e = [abs(x_ - x_final) for x_ in x_list]
    q = [(log(e[n+1]/e[n]))/(log(e[n]/e[n-1])) for n in range(1, len(e)-1, 1)]
    return q

def print_rates( x_list, x_final):
    r = rate(x_list, x_final)
    q = ['%.2f' % q_ for q_ in r ]
    print ("Convergence rate : ",q)