import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def drawGraph(a,b,fx,err,x,f,markers,cv):
    cst=cv
    fig, ax = plt.subplots(2,1)
    fig.set_size_inches(9, 8)
    x_min=x[-4]
    y_avant_max=f(x[-3])
    x_info=x[2]
    y_info=f(x[-1])

    ax[1].plot(x, f(x),'m')
    ax[1].axhline(y=0, xmin=0.0, xmax=1.0, color='k')
    plt.ylim(bottom=-2)

    data=[]
    for x in markers[-10:] :
       data.append((x,f(x)))

    clust_data = np.random.random((2, 18))
    collabel = ('xn','f(xn)')
    ax[0].axis('tight')
    ax[0].axis('off')
    the_table = ax[0].table(cellText=data, colLabels=collabel, loc='center')



    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    if cv:
        cv= f'taux de convergence : {cv} \nf(x)=0 for x={x}'
    else:
        cv=f'f(x)=0 for x={x}'

    x_begin=x_min
    y_begin=y_avant_max+1
    plt.text(x_begin,y_begin, cv, horizontalalignment='center',
             verticalalignment='center', fontsize=12, color='k',bbox=props)

    if a!=b:
        info=f' f(x) = {fx} \nerror ={err} \n[{float(a)},{float(b)}]'
    else:
        info=f' f(x) = {fx} \nerror ={err} \n Xo = {a}'

    plt.text(x_info,y_info, info, horizontalalignment='center',
             verticalalignment='top', fontsize=12, color='k',bbox=props)

    plt.xticks(markers)

    i=1
    j = 0

    for x in markers:
        plt.scatter(x, f(x), marker='o',linestyle='--')

        if i>= len(markers)/20 and not cst:
            plt.xlim(x-0.4,x+0.4)
            j+=1
            if markers[-1]>x:
                plt.plot((a, x), (0,0), 'r-',linewidth=j%5+1)
                # plt.axhline(y=0,color='b',linestyle='-')
            else:
                plt.plot((x, b), (0,0), 'b-',linewidth=j%5+1)
                # plt.axhline(y=0,color='r',linestyle='-')
        else:
            plt.axvline(x=x, color='k', linestyle='--')

        i+=1
        try:
            plt.pause(3)
        except tk.TclError:
            break
