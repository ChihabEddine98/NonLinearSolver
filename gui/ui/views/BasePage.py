import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def drawGraph(a,b,fx,err,x,f,markers):
    fig, ax = plt.subplots(2,1)
    fig.set_size_inches(9, 8)

    ax[1].plot(x, f(x),'m')
    ax[1].axhline(y=0, xmin=0.0, xmax=1.0, color='k')
    plt.ylim(bottom=-2)

    data=[]
    i=0
    for x in markers :
        if i<10:
           data.append((x,f(x)))
        i+=1

    clust_data = np.random.random((2, 18))
    collabel = ('xn','f(xn)')
    ax[0].axis('tight')
    ax[0].axis('off')
    the_table = ax[0].table(cellText=data, colLabels=collabel, loc='center')



    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    cv= f'taux de convergence : {1.8} \nf(x)=0 for x={x}'

    plt.text(0.1,-2.4, cv, horizontalalignment='center',
             verticalalignment='center', fontsize=12, color='k',bbox=props)

    info=f' f(x) = {fx} \nerror ={err} \n[{int(a)},{int(b)}]'

    plt.text(0.12,-0.08, info, horizontalalignment='center',
             verticalalignment='top', fontsize=12, color='k',bbox=props)

    plt.xticks(markers)

    for x in markers:
        plt.scatter(x, f(x), marker='o',linestyle='--')
        if f(x)>0 :
            yMax=1
            yMin=0.8
        else:
            yMax=0.8
            yMin=0.4


        plt.axvline(x=x,color='k',linestyle='--')
        try:
            plt.pause(3)
        except tk.TclError:
            break
