from math import log



def rate(x_list, x_final):
    e = [abs(x_ - x_final) for x_ in x_list]
    print (e)
    q = [(log(e[n+1]/e[n]))/(log(e[n]/e[n-1])) for n in range(1, len(e)-1, 1)]
    return q


x_list = Newton(f, dfdx, x=1000, eps=1e-6, return_x_list=True)
def print_rates(method, x_list, x_final):
    q = ['%.2f' % q_ for q_ in rate(x_list, x_final)]
    print (method + ':')
    for q_ in q:
        print(q_)
    print()
#print(rate([-3,-2.391304347826087,-2.1549635442373654, -2.1159454947237117, -2.114908266449071],-2.11490754147711))
list=[  2.0
,1.6666666666666667
,1.8363636363636364,1.8656905800830403
,1.860700078777279, 1.8608054030708354
, 1.8608058531533074]
print_rates('Newton',list , 1.860805853111703)