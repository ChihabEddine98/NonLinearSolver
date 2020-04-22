from math import log

def rate(x, x_exact):
    e = [abs(x_ - x_exact) for x_ in x]
    print (e)
    q = [(log(e[n+1]/e[n]))/(log(e[n]/e[n-1])) for n in range(4)]
    return q


print(rate([-3,-2.391304347826087,-2.1549635442373654, -2.1159454947237117, -2.114908266449071],-2.11490754147711))