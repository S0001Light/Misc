from tkinter import *
import tkinter as tk

App = Tk()
App.config(bg="#000000")
App.title('Tip Calculator')

TotalCostOfReciept = Label(App, text='Total Of Receipt')
TotalCostOfReciept.config(bg="#000000", fg="#ffffff")
TotalCostOfReciept.grid(row=0, column=0)
costOf = IntVar()
TotalCost = Entry(App, textvariable=costOf)
TotalCost.grid(row=1, column=0)

PercentCost = Label(App, text='dot what of Total')
PercentCost.config(bg="#000000", fg="#ffffff")
PercentCost.grid(row=2, column=0)
percentOf = DoubleVar()
percentOfCost = Entry(App, textvariable=percentOf)
percentOfCost.grid(row=3, column=0)

def receiptTip():

    costs = float(TotalCost.get())
    percents = percentOfCost.get()
    percentTo = float(percents)
    tipCost = costs * percentTo
    tipFunction = varText.set(tipCost)
    tipFunction
    return

updateT_text = Button(App, width=8, command=receiptTip, text="Calculate")
updateT_text.grid(row=4, column=0)
varText = IntVar()
updated_text = Entry(App, textvariable=varText)
updated_text.grid(row=5, column=0)

App.mainloop()
