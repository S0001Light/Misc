from tkinter import *
import tkinter as tk
from math import *

App = Tk()
App.config(bg="#000000")
App.title('Pi - Area of a circle')

AlgbrAddPlus0 = Label(App, text='PI - Area of a circle')
AlgbrAddPlus0.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus0.grid(row=0, column=0)

AlgbrAddPlus1 = Label(App, text='Radius Of Circle')
AlgbrAddPlus1.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus1.grid(row=1, column=0)
addPlus1 = IntVar()
AlgbrAdd1 = Entry(App, textvariable=addPlus1)
AlgbrAdd1.grid(row=2, column=0)

def piAdd():
        firstNumeral = float(AlgbrAdd1.get())
        firstAdd = pi * firstNumeral**2
        varText.set(firstAdd)
	

updateT_text = Button(App, width=8, command=piAdd, text="Calculate")
updateT_text.grid(row=3, column=0)
varText = IntVar()
updated_text = Entry(App, textvariable=varText)
updated_text.grid(row=4, column=0)

App.mainloop

