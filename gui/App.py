
import tkinter as tk
from tkinter import font  as tkfont

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.resizable(width=False, height=False)
        self.title("Systemes Non Linéaires")
        self.geometry("935x695+300+50")


        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, DichotomiePage, NewtonPage,CordesPage,FalsePosPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Systemes Non Lineaires " , font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        btn_dicho = tk.Button(self, text="Dichotomie",
                            command=lambda: controller.show_frame("DichotomiePage"))
        btn_newton = tk.Button(self, text="Newton",
                            command=lambda: controller.show_frame("NewtonPage"))
        btn_cordes = tk.Button(self, text="Cordes",
                            command=lambda: controller.show_frame("CordesPage"))
        btn_falsePos = tk.Button(self, text="Fausse Position",
                            command=lambda: controller.show_frame("FalsePosPage"))

        btn_dicho.pack()
        btn_newton.pack()
        btn_cordes.pack()
        btn_falsePos.pack()


class DichotomiePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Méthode De dichotomie", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()


class NewtonPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Méthode de Newton", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()

class CordesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Méthode de Cordes", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()

class FalsePosPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Méthode de Fausse Position ", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="retour",
                           command=lambda: controller.show_frame("HomePage"))
        button.pack()
