import tkinter as tk


class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        font13 = "-family {Tw Cen MT} -size 18"
        font14 = "-family {Tw Cen MT} -size 22"

        self.configure(background="#000")

        self.Frame1 = tk.Frame(self)
        self.Frame1.place(relx=0.034, rely=0.182, relheight=0.549
                          , relwidth=0.529)
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=-0.064, rely=0.275, height=74, width=368)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(text='''Non Linear Equation''')

        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.278, rely=0.441, height=44, width=233)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#000")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font=font14)
        self.Label1_1.configure(foreground="#00ff00")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Solver''')

        self.Frame2 = tk.Frame(self)
        self.Frame2.place(relx=0.566, rely=0.242, relheight=0.514
                          , relwidth=0.292)
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#000")

        self.btnDicho = tk.Button(self.Frame2)
        self.btnDicho.place(relx=0.078, rely=0.059, height=53, width=206)
        self.btnDicho.configure(activebackground="#80ff00")
        self.btnDicho.configure(activeforeground="#000000")
        self.btnDicho.configure(background="#000")
        self.btnDicho.configure(borderwidth="3")
        self.btnDicho.configure(cursor="fleur")
        self.btnDicho.configure(disabledforeground="#a3a3a3")
        self.btnDicho.configure(font=font13)
        self.btnDicho.configure(foreground="#fff")
        self.btnDicho.configure(highlightbackground="#ffff00")
        self.btnDicho.configure(highlightcolor="black")
        self.btnDicho.configure(pady="0")
        self.btnDicho.configure(relief="ridge")
        self.btnDicho.configure(text='''Dichotomie''')
        self.btnDicho.configure(command=lambda: controller.show_frame("DichotomiePage"))

        self.btnNewton = tk.Button(self.Frame2)
        self.btnNewton.place(relx=0.078, rely=0.265, height=53, width=206)
        self.btnNewton.configure(activebackground="#80ff00")
        self.btnNewton.configure(activeforeground="#000000")
        self.btnNewton.configure(background="#000")
        self.btnNewton.configure(borderwidth="3")
        self.btnNewton.configure(disabledforeground="#a3a3a3")
        self.btnNewton.configure(font=font13)
        self.btnNewton.configure(foreground="#fff")
        self.btnNewton.configure(highlightbackground="#d9d9d9")
        self.btnNewton.configure(highlightcolor="black")
        self.btnNewton.configure(pady="0")
        self.btnNewton.configure(relief="ridge")
        self.btnNewton.configure(text='''Newton''')
        self.btnNewton.configure(command= lambda : controller.show_frame("NewtonPage"))


        self.btnFausse = tk.Button(self.Frame2)
        self.btnFausse.place(relx=0.078, rely=0.676, height=53, width=206)
        self.btnFausse.configure(activebackground="#80ff00")
        self.btnFausse.configure(activeforeground="#000000")
        self.btnFausse.configure(background="#000")
        self.btnFausse.configure(borderwidth="3")
        self.btnFausse.configure(disabledforeground="#a3a3a3")
        self.btnFausse.configure(font=font13)
        self.btnFausse.configure(foreground="#fff")
        self.btnFausse.configure(highlightbackground="#d9d9d9")
        self.btnFausse.configure(highlightcolor="black")
        self.btnFausse.configure(pady="0")
        self.btnFausse.configure(relief="ridge")
        self.btnFausse.configure(text='''Fausse Position''')
        self.btnFausse.configure(command= lambda : controller.show_frame("FalsePosPage"))


        self.btnCordes = tk.Button(self.Frame2)
        self.btnCordes.place(relx=0.078, rely=0.471, height=53, width=206)
        self.btnCordes.configure(activebackground="#80ff00")
        self.btnCordes.configure(activeforeground="#000000")
        self.btnCordes.configure(background="#000")
        self.btnCordes.configure(borderwidth="3")
        self.btnCordes.configure(disabledforeground="#a3a3a3")
        self.btnCordes.configure(font=font13)
        self.btnCordes.configure(foreground="#fff")
        self.btnCordes.configure(highlightbackground="#d9d9d9")
        self.btnCordes.configure(highlightcolor="black")
        self.btnCordes.configure(pady="0")
        self.btnCordes.configure(relief="ridge")
        self.btnCordes.configure(text='''Cordes''')
        self.btnCordes.configure(command= lambda : controller.show_frame("CordesPage"))
