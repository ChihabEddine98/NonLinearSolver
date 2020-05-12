from math import log


def rate(x_list, x_final):
    e = [abs(x_ - x_final) for x_ in x_list]
    q = [(log(e[n+1]/e[n]))/(log(e[n]/e[n-1])) for n in range(1, len(e)-1, 1)]
    return q


def print_rates_list(x_list, x_final):
    r = rate(x_list, x_final)
    q = ['%.2f' % q_ for q_ in r]
    print("Convergence rate list : ", q)


def print_rate(x_list):
    x_final = x_list[-1]
    # remove doublon,susceptible de faire crasher le rate
    x_list = list(dict.fromkeys(x_list))
    x_list.pop()
    r=rate(x_list, x_final)
    q = ['%.2f' % q_ for q_ in r]
    print("Convergence rate : ",q[-1])
