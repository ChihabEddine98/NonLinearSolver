import tkinter as tk
import numpy as np
import matplotlib as mp
mp.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import time
import matplotlib.pyplot as plt




from algos.Dichotomie import *
from algos.Equa_Solver import *


def drawGraph(x,f,markers):
    fig, ax = plt.subplots()

    ax.plot(x, f(x),'m')
    ax.axhline(y=0, xmin=0.0, xmax=1.0, color='k')
    plt.ylim(bottom=-2)

    for x in markers:
        plt.scatter(x, f(x), marker='o')
        try:
            plt.pause(1)
        except tk.TclError:
            break



class DichotomiePage(tk.Frame):

    def test1(self):
        fx = "x**2-math.cos(x)"
        f = lambda x: eval("x**2-np.cos(x)")

        equa=Equa_Solver(f=fx,a=0,b=1,err=1e-15)
        dichoRes=Dichotomie.solve(equa)
        t = np.linspace(0, 1, 10)
        fig=Figure(figsize=(5,5),dpi=100)
        a = fig.add_subplot(111)
        a.plot(t, f(t), 'm')
        canvas=FigureCanvasTkAgg(fig,self)
        toolbar=NavigationToolbar2TkAgg(canvas,self)
        toolbar.update()
        #canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
        canvas.get_tk_widget().place(relx=0.17, rely=0.35, height=415, width=600)

        # ax.plot(x, f(x), 'm')
        # ax.axhline(y=0, xmin=0.0, xmax=1.0, color='k')
        # a.ylim(bottom=-2)

        for x in dichoRes:
            a.scatter(x, f(x), marker='o')


        # drawGraph(t,f,dichoRes)

        # f=Figure(figsize=(5,5),dpi=100)
        # a=f.add_subplot(111)
        # a.plot([1,2,3,4,5],[2,-2,6,7,3])
        # canvas=FigureCanvasTkAgg(f,self)





    def __init__(self,parent,controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        font11 = "-family {Tw Cen MT} -size 20"
        font12 = "-family {Tw Cen MT} -size 23"
        font14 = "-family {Yu Gothic UI Semibold} -size 24 -weight "  \
            "bold"

        self.mainFrame = tk.Frame(self)
        self.mainFrame.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.mainFrame.configure(relief='groove')
        self.mainFrame.configure(borderwidth="2")
        self.mainFrame.configure(relief="groove")
        self.mainFrame.configure(background="#000")
        self.mainFrame.configure(highlightbackground="#d9d9d9")
        self.mainFrame.configure(highlightcolor="black")

        self.titleFrame = tk.Frame(self.mainFrame)
        self.titleFrame.place(relx=0.487, rely=0.0, relheight=0.088
                , relwidth=0.519)
        self.titleFrame.configure(relief="groove")
        self.titleFrame.configure(background="#000")
        self.titleFrame.configure(highlightbackground="#d9d9d9")
        self.titleFrame.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.titleFrame)
        self.Label1.place(relx=-0.02, rely=0.156, height=40, width=460)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Tw Cen MT} -size 23")
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Méthode De dichotomie''')

        self.Frame1 = tk.Frame(self.mainFrame)
        self.Frame1.place(relx=0.083, rely=0.082, relheight=0.28, relwidth=0.821)

        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.entryFomule = tk.Entry(self.Frame1)
        self.entryFomule.place(relx=0.227, rely=0.294, height=54, relwidth=0.736)

        self.entryFomule.configure(background="#000")
        self.entryFomule.configure(disabledforeground="#a3a3a3")
        self.entryFomule.configure(font="-family {Tw Cen MT} -size 20")
        self.entryFomule.configure(foreground="#00ff00")
        self.entryFomule.configure(highlightbackground="#d9d9d9")
        self.entryFomule.configure(highlightcolor="black")
        self.entryFomule.configure(insertbackground="black")
        self.entryFomule.configure(relief="groove")
        self.entryFomule.configure(selectbackground="#c4c4c4")
        self.entryFomule.configure(selectforeground="black")

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.277, rely=0.049, height=31, width=321)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#000")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Tw Cen MT} -size 20")
        self.Label2.configure(foreground="#fff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Entrez la formule :''')

        self.btnSolve = tk.Button(self.Frame1)
        self.btnSolve.place(relx=0.296, rely=0.637, height=53, width=276)
        self.btnSolve.configure(activebackground="#80ff00")
        self.btnSolve.configure(activeforeground="#000000")
        self.btnSolve.configure(background="#000")
        self.btnSolve.configure(disabledforeground="#a3a3a3")
        self.btnSolve.configure(font="-family {Tw Cen MT} -size 20")
        self.btnSolve.configure(foreground="#fff")
        self.btnSolve.configure(highlightbackground="#d9d9d9")
        self.btnSolve.configure(highlightcolor="black")
        self.btnSolve.configure(pady="0")
        self.btnSolve.configure(relief="groove")
        self.btnSolve.configure(text='''Solve''')
        self.btnSolve.configure(command= lambda : self.test1())


        self.Label2_10 = tk.Label(self.Frame1)
        self.Label2_10.place(relx=0.076, rely=0.343, height=31, width=100)
        self.Label2_10.configure(activebackground="#f9f9f9")
        self.Label2_10.configure(activeforeground="black")
        self.Label2_10.configure(background="#000")
        self.Label2_10.configure(disabledforeground="#a3a3a3")
        self.Label2_10.configure(font="-family {Yu Gothic UI Semibold} -size 24 -weight bold")
        self.Label2_10.configure(foreground="#fff")
        self.Label2_10.configure(highlightbackground="#d9d9d9")
        self.Label2_10.configure(highlightcolor="black")
        self.Label2_10.configure(text='''f(x) =''')

        self.btnRetour = tk.Button(self.mainFrame)
        self.btnRetour.place(relx=0.021, rely=0.014, height=43, width=186)
        self.btnRetour.configure(activebackground="#80ff00")
        self.btnRetour.configure(activeforeground="#000000")
        self.btnRetour.configure(background="#b0b8ce")
        self.btnRetour.configure(disabledforeground="#a3a3a3")
        self.btnRetour.configure(font="-family {Tw Cen MT} -size 20")
        self.btnRetour.configure(foreground="#000")
        self.btnRetour.configure(highlightbackground="#d9d9d9")
        self.btnRetour.configure(highlightcolor="black")
        self.btnRetour.configure(pady="0")
        self.btnRetour.configure(relief="groove")
        self.btnRetour.configure(text='''Go Back''')
        self.btnRetour.configure(command=lambda: controller.show_frame("WelcomePage"))



class DichotomiePage2(tk.Frame):

    def test1(self):
        fx = "x**2-math.cos(x)"
        f = lambda x: eval("x**2-np.cos(x)")

        equa=Equa_Solver(f=fx,a=0,b=1,err=1e-15)
        dichoRes=Dichotomie.solve(equa)
        t = np.linspace(0, 1, 10)
        drawGraph(t,f,dichoRes)

    def test2(self):
        fx="x**3 - x**2 - 1"
        f = lambda x: eval(fx)

        equa=Equa_Solver(f=fx,a=1,b=2,err=1e-8)
        dichoRes=Dichotomie.solve(equa)
        t = np.linspace(1, 2, 10)
        drawGraph(t,f,dichoRes)

    def test3(self):
        fx="math.cos(2*x)**2 - x**2"
        f= lambda x:eval("np.cos(2*x)**2 - x**2")

        equa=Equa_Solver(f=fx,a=0,b=2,err=1e-8)
        dichoRes=Dichotomie.solve(equa)
        t = np.linspace(0, 2, 10)
        drawGraph(t,f,dichoRes)

    def test4(self):
        fx="math.cos(x)"
        f= lambda x:eval("np.cos(x)")

        equa=Equa_Solver(f=fx,a=0,b=2,err=1e-14)
        dichoRes=Dichotomie.solve(equa)
        t = np.linspace(0, 2, 10)
        drawGraph(t,f,dichoRes)

    def test5(self):
        fx = "x**3 - 4*x + 1"
        f = lambda x: eval("x**3 - 4*x + 1")

        equa = Equa_Solver(f=fx, a=0, b=1, err=1e-14)
        dichoRes = Dichotomie.solve(equa)
        t = np.linspace(0, 1, 10)
        drawGraph(t, f, dichoRes)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Méthode De dichotomie", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        btntst1 = tk.Button(self, text="f(x)= x²-cos(x)",
                           command=lambda: self.test1())
        btntst2 = tk.Button(self, text="f(x)= x^3-x²-1",
                           command=lambda: self.test2())
        btntst3 = tk.Button(self, text="f(x)= cos²(2x)-x²",
                           command=lambda: self.test3())

        btntst4 = tk.Button(self, text="f(x)= cos(x)",
                           command=lambda: self.test4())
        btntst5 = tk.Button(self, text="f(x)= x^3-4x+1",
                           command=lambda: self.test5())

        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("HomePage"))
        btntst1.pack()
        btntst2.pack()
        btntst3.pack()
        btntst4.pack()
        btntst5.pack()
        button.pack()