import subprocess
subprocess.call("cls",shell=True)
from tkinter import *
from tkinter import messagebox
from random import *
from tkinter import ttk
import numpy as np

def Fasl():

    p1=Tk()
    p1.title("Fasl")
    p1.geometry("1000x700")
    p1.config(bg="#B6F6EB")

    v=StringVar()

    combo1=ttk.Combobox(p1,textvariable=v)
    combo1.set("persian fasl")
    combo1.place(x=400,y=10)

    v2=StringVar()

    combo2=ttk.Combobox(p1,textvariable=v2)
    combo2.set("english fasl")
    combo2.place(x=400,y=50)
    combo2["values"]

    p1.mainloop()
Fasl()