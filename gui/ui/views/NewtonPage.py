import tkinter as tk
from tkinter.messagebox import showerror
import numpy as np
import matplotlib as mp
# mp.use("TkAgg")
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
# from matplotlib.figure import Figure
import time
import matplotlib.pyplot as plt




from algos.Newton import *
from algos.Equa_Solver import *
from .BasePage import drawGraph
from convergence_rate import *


# def drawGraphInWindow(t,f,self):
#     fig = Figure(figsize=(5, 5), dpi=100)
#     a = fig.add_subplot(111)
#     a.plot(t, f(t), 'm')
#     canvas = FigureCanvasTkAgg(fig, self)
#     toolbar = NavigationToolbar2TkAgg(canvas, self)
#     toolbar.update()
#     # canvas._tkcanvas.pack(side=tk.TOP,fill=tk.BOTH,expand=True)
#     canvas.get_tk_widget().place(relx=0.17, rely=0.35, height=415, width=600)


class NewtonPage(tk.Frame):

    def test1(self):
        formule=self.entryFomule.get()
        fx=formule

        err=float(self.entryErr.get()) if self.entryErr.get() else 1e-10

        try:
            f = lambda x: eval(fx)

            x0 = float(self.entryA.get())


            if self.entryFomule_df.get():
                dfx=self.entryFomule_df
                equa = Newton(f=fx, df=dfx,x0=x0, err=err,max_iter=10)

            else:
                equa = Newton(f=fx, x0=x0, err=err, max_iter=10)

            newtonRes = Newton.solve(equa)
            newtonRes_final=newtonRes[-1]
            newtonRes.pop()
            t = np.linspace(x0, 3, 10)
            cv=rate(newtonRes,newtonRes_final)[-1].__format__('.2f')
            drawGraph(x0,x0,fx,err,t, f, newtonRes,cv=cv)


        except ValueError as verr:
           print(verr.with_traceback())
           showerror(title=" Intervalle érroné", message=" Le Xo doit etre un nombre   !")
           return
        except (TypeError ,SyntaxError ) as e:
            if type(e)== TypeError :
                showerror(title=" Max iter Dépassé ", message=" Oops ! on vient de dépassé le max_iter donné ")
            else:
                showerror(title=" Formule érronée", message=" La fonction que vous avez entré n'est pas correcte !")

            return
        except SolverException:
            showerror(title=" monotonie !", message=" La fonction que vous avez entré n'est pas monotonne \n f(a)*f(b) > 0 !")
            return
        except Exception as ex:
            print(ex)
            showerror(title=" Oops error!", message=" Just be sure from your inputs.")
            return


        # ax.plot(x, f(x), 'm')
        # ax.axhline(y=0, xmin=0.0, xmax=1.0, color='k')
        # a.ylim(bottom=-2)


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
        self.titleFrame.place(relx=0.186, rely=-0.026, relheight=0.101
                , relwidth=0.658)
        self.titleFrame.configure(relief="groove")
        self.titleFrame.configure(background="#000")
        self.titleFrame.configure(highlightbackground="#d9d9d9")
        self.titleFrame.configure(highlightcolor="black")

        self.Label1 = tk.Label(self.titleFrame)
        self.Label1.place(relx=0.134, rely=0.208, height=82, width=412)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#000")
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Tw Cen MT} -size 23")
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Méthode De Newton''')

        self.Frame1 = tk.Frame(self.mainFrame)
        self.Frame1.place(relx=0.083, rely=0.079, relheight=0.789
                , relwidth=0.817)
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.entryFomule = tk.Entry(self.Frame1)
        self.entryFomule.place(relx=0.038, rely=0.117, height=54, relwidth=0.918)

        self.entryFomule.configure(background="#000")
        self.entryFomule.configure(disabledbackground="#9bd2aa")
        self.entryFomule.configure(disabledforeground="#a3a3a3")
        self.entryFomule.configure(font="-family {Tw Cen MT} -size 20")
        self.entryFomule.configure(foreground="#00ff00")
        self.entryFomule.configure(highlightbackground="#00ff00")
        self.entryFomule.configure(highlightcolor="#00ff00")
        self.entryFomule.configure(highlightthickness="1")
        self.entryFomule.configure(insertbackground="#00ff00")
        self.entryFomule.configure(insertborderwidth="1")
        self.entryFomule.configure(relief="flat")
        self.entryFomule.configure(selectbackground="#c4c4c4")
        self.entryFomule.configure(selectforeground="black")

        self.btnSolve = tk.Button(self.Frame1)
        self.btnSolve.place(relx=0.567, rely=0.778, height=53, width=276)
        self.btnSolve.configure(activebackground="#80ff00")
        self.btnSolve.configure(activeforeground="#000000")
        self.btnSolve.configure(background="#000")
        self.btnSolve.configure(cursor="arrow")
        self.btnSolve.configure(disabledforeground="#a3a3a3")
        self.btnSolve.configure(font="-family {Tw Cen MT} -size 20")
        self.btnSolve.configure(foreground="#fff")
        self.btnSolve.configure(highlightbackground="#00ff00")
        self.btnSolve.configure(highlightcolor="#00ff00")
        self.btnSolve.configure(highlightthickness="2")
        self.btnSolve.configure(pady="0")
        self.btnSolve.configure(relief="ridge")
        self.btnSolve.configure(text='''Solve''')

        self.Label2_10 = tk.Label(self.Frame1)
        self.Label2_10.place(relx=0.418, rely=0.017, height=49, width=98)
        self.Label2_10.configure(activebackground="#f9f9f9")
        self.Label2_10.configure(activeforeground="black")
        self.Label2_10.configure(background="#000")
        self.Label2_10.configure(disabledforeground="#a3a3a3")
        self.Label2_10.configure(font="-family {Yu Gothic UI Semibold} -size 24 -weight bold")
        self.Label2_10.configure(foreground="#fff")
        self.Label2_10.configure(highlightbackground="#d9d9d9")
        self.Label2_10.configure(highlightcolor="black")
        self.Label2_10.configure(text='''f(x)''')

        self.entryA = tk.Entry(self.Frame1)
        self.entryA.place(relx=0.038, rely=0.557,height=54, relwidth=0.423)
        self.entryA.configure(background="#000")
        self.entryA.configure(cursor="fleur")
        self.entryA.configure(disabledbackground="#9bd2aa")
        self.entryA.configure(disabledforeground="#a3a3a3")
        self.entryA.configure(font="-family {Tw Cen MT} -size 20")
        self.entryA.configure(foreground="#00ff00")
        self.entryA.configure(highlightbackground="#00ff00")
        self.entryA.configure(highlightcolor="#00ff00")
        self.entryA.configure(highlightthickness="1")
        self.entryA.configure(insertbackground="#00ff00")
        self.entryA.configure(insertborderwidth="1")
        self.entryA.configure(relief="flat")
        self.entryA.configure(selectbackground="#c4c4c4")
        self.entryA.configure(selectforeground="black")

        self.Label2_2 = tk.Label(self.Frame1)
        self.Label2_2.place(relx=0.151, rely=0.443, height=46, width=89)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#000")
        self.Label2_2.configure(cursor="fleur")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(font="-family {Yu Gothic UI Semibold} -size 24 -weight bold")
        self.Label2_2.configure(foreground="#fff")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''Xo''')

        # self.Label2_3 = tk.Label(self.Frame1)
        # self.Label2_3.place(relx=0.692, rely=0.443, height=46, width=80)
        # self.Label2_3.configure(activebackground="#f9f9f9")
        # self.Label2_3.configure(activeforeground="black")
        # self.Label2_3.configure(background="#000")
        # self.Label2_3.configure(disabledforeground="#a3a3a3")
        # self.Label2_3.configure(font="-family {Yu Gothic UI Semibold} -size 24 -weight bold")
        # self.Label2_3.configure(foreground="#fff")
        # self.Label2_3.configure(highlightbackground="#d9d9d9")
        # self.Label2_3.configure(highlightcolor="black")
        # self.Label2_3.configure(text='''b''')
        #
        # self.entryB = tk.Entry(self.Frame1)
        # self.entryB.place(relx=0.541, rely=0.557,height=54, relwidth=0.423)
        # self.entryB.configure(background="#000")
        # self.entryB.configure(cursor="fleur")
        # self.entryB.configure(disabledbackground="#9bd2aa")
        # self.entryB.configure(disabledforeground="#a3a3a3")
        # self.entryB.configure(font="-family {Tw Cen MT} -size 20")
        # self.entryB.configure(foreground="#00ff00")
        # self.entryB.configure(highlightbackground="#00ff00")
        # self.entryB.configure(highlightcolor="#00ff00")
        # self.entryB.configure(highlightthickness="1")
        # self.entryB.configure(insertbackground="#00ff00")
        # self.entryB.configure(insertborderwidth="1")
        # self.entryB.configure(relief="flat")
        # self.entryB.configure(selectbackground="#c4c4c4")
        # self.entryB.configure(selectforeground="black")

        self.entryErr = tk.Entry(self.Frame1)
        self.entryErr.place(relx=0.049, rely=0.778,height=54, relwidth=0.423)
        self.entryErr.configure(background="#000")
        self.entryErr.configure(disabledbackground="#9bd2aa")
        self.entryErr.configure(disabledforeground="#a3a3a3")
        self.entryErr.configure(font="-family {Tw Cen MT} -size 20")
        self.entryErr.configure(foreground="#00ff00")
        self.entryErr.configure(highlightbackground="#00ff00")
        self.entryErr.configure(highlightcolor="#00ff00")
        self.entryErr.configure(highlightthickness="1")
        self.entryErr.configure(insertbackground="#00ff00")
        self.entryErr.configure(insertborderwidth="1")
        self.entryErr.configure(relief="flat")
        self.entryErr.configure(selectbackground="#c4c4c4")
        self.entryErr.configure(selectforeground="black")

        self.Label2_3 = tk.Label(self.Frame1)
        self.Label2_3.place(relx=0.013, rely=0.683, height=45, width=150)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#000")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(font="-family {Yu Gothic UI Semibold} -size 24 -weight bold")
        self.Label2_3.configure(foreground="#fff")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''Error''')

        self.entryFomule_df = tk.Entry(self.Frame1)
        self.entryFomule_df.place(relx=0.038, rely=0.348, height=54
                , relwidth=0.918)
        self.entryFomule_df.configure(background="#000")
        self.entryFomule_df.configure(disabledbackground="#9bd2aa")
        self.entryFomule_df.configure(disabledforeground="#a3a3a3")
        self.entryFomule_df.configure(font="-family {Tw Cen MT} -size 20")
        self.entryFomule_df.configure(foreground="#00ff00")
        self.entryFomule_df.configure(highlightbackground="#00ff00")
        self.entryFomule_df.configure(highlightcolor="#00ff00")
        self.entryFomule_df.configure(highlightthickness="1")
        self.entryFomule_df.configure(insertbackground="#00ff00")
        self.entryFomule_df.configure(insertborderwidth="1")
        self.entryFomule_df.configure(relief="flat")
        self.entryFomule_df.configure(selectbackground="#c4c4c4")
        self.entryFomule_df.configure(selectforeground="black")

        self.Label2_5 = tk.Label(self.Frame1)
        self.Label2_5.place(relx=0.431, rely=0.233, height=39, width=89)
        self.Label2_5.configure(activebackground="#f9f9f9")
        self.Label2_5.configure(activeforeground="black")
        self.Label2_5.configure(background="#000")
        self.Label2_5.configure(disabledforeground="#a3a3a3")
        self.Label2_5.configure(font="-family {Yu Gothic UI Semibold} -size 24 -weight bold")
        self.Label2_5.configure(foreground="#fff")
        self.Label2_5.configure(highlightbackground="#d9d9d9")
        self.Label2_5.configure(highlightcolor="black")
        self.Label2_5.configure(text='''f'(x)''')

        self.btnRetour = tk.Button(self.mainFrame)
        self.btnRetour.place(relx=0.031, rely=0.908, height=43, width=186)
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
        self.btnSolve.configure(command= lambda : self.test1())
        self.btnRetour.configure(command=lambda: controller.show_frame("WelcomePage"))
