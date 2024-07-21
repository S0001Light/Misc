from tkinter import *
import tkinter as tk

App = Tk()
App.config(bg="#000000")
App.title('scs Algebra 3')
App.geometry('146x400')

AlgbrAddPlus0 = Label(App, text='Algebra - (1 # 1) # (1 # 1) # 1')
AlgbrAddPlus0.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus0.grid(row=0, column=0)

AlgbrAddPlus1 = Label(App, text='First Number')
AlgbrAddPlus1.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus1.grid(row=1, column=0)
addPlus1 = IntVar()
AlgbrAdd1 = Entry(App, textvariable=addPlus1)
AlgbrAdd1.grid(row=2, column=0)

AlgbrAddPlus2 = Label(App, text='Math Symbol 1')
AlgbrAddPlus2.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus2.grid(row=3, column=0)
addPlus2 = StringVar()
AlgbrAdd2 = Entry(App, textvariable=addPlus2)
AlgbrAdd2.grid(row=4, column=0)

AlgbrAddPlus3 = Label(App, text='Second Number')
AlgbrAddPlus3.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus3.grid(row=5, column=0)
addPlus3 = IntVar()
AlgbrAdd3 = Entry(App, textvariable=addPlus3)
AlgbrAdd3.grid(row=6, column=0)

AlgbrAddPlus4 = Label(App, text='Math Symbol 3')
AlgbrAddPlus4.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus4.grid(row=7, column=0)
addPlus4 = StringVar()
AlgbrAdd4 = Entry(App, textvariable=addPlus4)
AlgbrAdd4.grid(row=8, column=0)

AlgbrAddPlus5 = Label(App, text='Third Number')
AlgbrAddPlus5.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus5.grid(row=9, column=0)
addPlus5 = IntVar()
AlgbrAdd5 = Entry(App, textvariable=addPlus5)
AlgbrAdd5.grid(row=10, column=0)

AlgbrAddPlus6 = Label(App, text='Math Symbol 2')
AlgbrAddPlus6.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus6.grid(row=11, column=0)
addPlus6 = StringVar()
AlgbrAdd6 = Entry(App, textvariable=addPlus6)
AlgbrAdd6.grid(row=12, column=0)

AlgbrAddPlus7 = Label(App, text='Fourth Number')
AlgbrAddPlus7.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus7.grid(row=13, column=0)
addPlus7 = IntVar()
AlgbrAdd7 = Entry(App, textvariable=addPlus7)
AlgbrAdd7.grid(row=14, column=0)

AlgbrAddPlus8 = Label(App, text='Math Symbol 4')
AlgbrAddPlus8.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus8.grid(row=15, column=0)
addPlus8 = StringVar()
AlgbrAdd8 = Entry(App, textvariable=addPlus8)
AlgbrAdd8.grid(row=16, column=0)

AlgbrAddPlus9 = Label(App, text='Fifth Number')
AlgbrAddPlus9.config(bg="#000000", fg="#ffffff")
AlgbrAddPlus9.grid(row=17, column=0)
addPlus9 = IntVar()
AlgbrAdd9 = Entry(App, textvariable=addPlus9)
AlgbrAdd9.grid(row=18, column=0)

def algebraAdd():
        firstNumeral = float(AlgbrAdd1.get())
        secondNumeral = float(AlgbrAdd3.get())
        thirdNumeral = float(AlgbrAdd5.get())
        fourthNumeral = float(AlgbrAdd7.get())
        fifthNumeral = float(AlgbrAdd9.get())

        firstMathSign = AlgbrAdd2.get()
        thirdMathSign = AlgbrAdd4.get()
        secondMathSign = AlgbrAdd6.get()
        fourthMathSign = AlgbrAdd8.get()

        if firstMathSign == '+':
            firstAdd = firstNumeral + secondNumeral
            if secondMathSign == '+':
                secondAdd = thirdNumeral + fourthNumeral
                if thirdMathSign == '+':
                    thirdAdd = firstAdd + secondAdd
                    if fourthMathSign == "+":
                            fourthAdd = thirdAdd + fifthNumeral
                            varText.set(fourthAdd)
                    if fourthMathSign == "-":
                            fourthSub = thirdAdd - fifthNumeral
                            varText.set(fourthSub)
                    if fourthMathSign == "/":
                            fourthDiv = thirdAdd / fifthNumeral
                            varText.set(fourthDiv)
                    if fourthMathSign == "*":
                            fourthMulti = thirdAdd * fifthNumeral
                            varText.set(fourthMulti)
                            
                if thirdMathSign == '-':
                    thirdSub = firstAdd - secondAdd
                    if fourthMathSign == "+":
                            fourthAdd = thirdSub + fifthNumeral
                            varText.set(fourthAdd)
                    if fourthMathSign == "-":
                            fourthSub = thirdSub - fifthNumeral
                            varText.set(fourthSub)
                    if fourthMathSign == "/":
                            fourthDiv = thirdSub / fifthNumeral
                            varText.set(fourthDiv)
                    if fourthMathSign == "*":
                            fourthMulti = thirdSub * fifthNumeral
                            varText.set(fourthMulti)
                            
                if thirdMathSign == '/':
                    thirdDiv = firstAdd / secondAdd
                    if fourthMathSign == "+":
                            fourthAdd = thirdDiv + fifthNumeral
                            varText.set(fourthAdd)
                    if fourthMathSign == "-":
                            fourthSub = thirdDiv - fifthNumeral
                            varText.set(fourthSub)
                    if fourthMathSign == "/":
                            fourthDiv = thirdDiv / fifthNumeral
                            varText.set(fourthDiv)
                    if fourthMathSign == "*":
                            fourthMulti = thirdDiv * fifthNumeral
                            varText.set(fourthMulti)
                            
                if thirdMathSign == '*':
                    thirdMulti = firstAdd * secondAdd
                    if fourthMathSign == "+":
                            fourthAdd = thirdMulti + fifthNumeral
                            varText.set(fourthAdd)
                    if fourthMathSign == "-":
                            fourthSub = thirdMulti - fifthNumeral
                            varText.set(fourthSub)
                    if fourthMathSign == "/":
                            fourthDiv = thirdMulti / fifthNumeral
                            varText.set(fourthDiv)
                    if fourthMathSign == "*":
                            fourthMulti = thirdMulti * fifthNumeral
                            varText.set(fourthMulti)
                            
            if secondMathSign == '-':
                secondSub = thirdNumeral - fourthNumeral
                if thirdMathSign == '+':
                    fourthAdd = firstAdd + secondSub
                    if fourthMathSign == "+":
                            fifthAdd = fourthAdd + fifthNumeral
                            varText.set(fifthAdd)
                    if fourthMathSign == "-":
                            fifthSub = fourthAdd - fifthNumeral
                            varText.set(fifthSub)
                    if fourthMathSign == "/":
                            fifthDiv = fourthAdd / fifthNumeral
                            varText.set(fifthDiv)
                    if fourthMathSign == "*":
                            fifthMulti = fourthAdd * fifthNumeral
                            varText.set(fifthMulti)

                if thirdMathSign == '-':
                    fourthSub = firstAdd - secondSub
                    if fourthMathSign == "+":
                            fifthAdd = fourthSub + fifthNumeral
                            varText.set(fifthAdd)
                    if fourthMathSign == "-":
                            fifthSub = fourthSub - fifthNumeral
                            varText.set(fifthSub)
                    if fourthMathSign == "/":
                            fifthDiv = fourthSub / fifthNumeral
                            varText.set(fifthDiv)
                    if fourthMathSign == "*":
                            fifthMulti = fourthSub * fifthNumeral
                            varText.set(fifthMulti)

                if thirdMathSign == '/':
                    fourthDiv = firstAdd / secondSub
                    if fourthMathSign == "+":
                            fifthAdd = fourthDiv + fifthNumeral
                            varText.set(fifthAdd)
                    if fourthMathSign == "-":
                            fifthSub = fourthDiv - fifthNumeral
                            varText.set(fifthSub)
                    if fourthMathSign == "/":
                            fifthDiv = fourthDiv / fifthNumeral
                            varText.set(fifthDiv)
                    if fourthMathSign == "*":
                            fifthMulti = fourthDiv * fifthNumeral
                            varText.set(fifthMulti)

                if thirdMathSign == '*':
                    fourthMulti = firstAdd * secondSub
                    if fourthMathSign == "+":
                            fifthAdd = fourthMulti + fifthNumeral
                            varText.set(fifthAdd)
                    if fourthMathSign == "-":
                            fifthSub = fourthMulti - fifthNumeral
                            varText.set(fifthSub)
                    if fourthMathSign == "/":
                            fifthDiv = fourthMulti / fifthNumeral
                            varText.set(fifthDiv)
                    if fourthMathSign == "*":
                            fifthMulti = fourthMulti * fifthNumeral
                            varText.set(fifthMulti)

            if secondMathSign == '/':
                secondDiv = thirdNumeral / fourthNumeral
                if thirdMathSign == '+':
                    eighthAdd = firstAdd + secondDiv
                    if fourthMathSign == "+":
                            ninthAdd = eighthAdd + fifthNumeral
                            varText.set(ninthAdd)
                    if fourthMathSign == "-":
                            ninthSub = eighthAdd - fifthNumeral
                            varText.set(ninthSub)
                    if fourthMathSign == "/":
                            ninthDiv = eighthAdd / fifthNumeral
                            varText.set(ninthDiv)
                    if fourthMathSign == "*":
                            ninthMulti = eighthAdd * fifthNumeral
                            varText.set(ninthMulti)

                if thirdMathSign == '-':
                    eighthSub = firstAdd - secondDiv
                    if fourthMathSign == "+":
                            ninthAdd = eighthSub + fifthNumeral
                            varText.set(ninthAdd)
                    if fourthMathSign == "-":
                            ninthSub = eighthSub - fifthNumeral
                            varText.set(ninthSub)
                    if fourthMathSign == "/":
                            ninthDiv = eighthSub / fifthNumeral
                            varText.set(ninthDiv)
                    if fourthMathSign == "*":
                            ninthMulti = eighthSub * fifthNumeral
                            varText.set(ninthMulti)

                if thirdMathSign == '/':
                    eighthDiv = firstAdd / secondDiv
                    if fourthMathSign == "+":
                            ninthAdd = eighthDiv + fifthNumeral
                            varText.set(ninthAdd)
                    if fourthMathSign == "-":
                            ninthSub = eighthDiv - fifthNumeral
                            varText.set(ninthSub)
                    if fourthMathSign == "/":
                            ninthDiv = eighthDiv / fifthNumeral
                            varText.set(ninthDiv)
                    if fourthMathSign == "*":
                            ninthMulti = eighthDiv * fifthNumeral
                            varText.set(ninthMulti)

                if thirdMathSign == '*':
                    eighthMulti = firstAdd * secondDiv
                    if fourthMathSign == "+":
                            ninthAdd = eighthMulti + fifthNumeral
                            varText.set(ninthAdd)
                    if fourthMathSign == "-":
                            ninthSub = eighthMulti - fifthNumeral
                            varText.set(ninthSub)
                    if fourthMathSign == "/":
                            ninthDiv = eighthMulti / fifthNumeral
                            varText.set(ninthDiv)
                    if fourthMathSign == "*":
                            ninthMulti = eighthMulti * fifthNumeral
                            varText.set(ninthMulti)
                            
            if secondMathSign == '*':
                secondMulti = thirdNumeral * fourthNumeral
                if thirdMathSign == '+':
                    tenthAdd = firstAdd + secondMulti
                    if fourthMathSign == "+":
                            eleventhAdd = tenthAdd + fifthNumeral
                            varText.set(eleventhAdd)
                    if fourthMathSign == "-":
                            eleventhSub = tenthAdd - fifthNumeral
                            varText.set(eleventhSub)
                    if fourthMathSign == "/":
                            eleventhDiv = tenthAdd / fifthNumeral
                            varText.set(eleventhDiv)
                    if fourthMathSign == "*":
                            eleventhMulti = tenthAdd * fifthNumeral
                            varText.set(eleventhMulti)

                if thirdMathSign == '-':
                    tenthSub = firstAdd - secondMulti
                    if fourthMathSign == "+":
                            eleventhAdd = tenthSub + fifthNumeral
                            varText.set(eleventhAdd)
                    if fourthMathSign == "-":
                            eleventhSub = tenthSub - fifthNumeral
                            varText.set(eleventhSub)
                    if fourthMathSign == "/":
                            eleventhDiv = tenthSub / fifthNumeral
                            varText.set(eleventhDiv)
                    if fourthMathSign == "*":
                            eleventhMulti = tenthSub * fifthNumeral
                            varText.set(eleventhMulti)

                if thirdMathSign == '/':
                    tenthDiv = firstAdd / secondMulti
                    if fourthMathSign == "+":
                            eleventhAdd = tenthDiv + fifthNumeral
                            varText.set(eleventhAdd)
                    if fourthMathSign == "-":
                            eleventhSub = tenthDiv - fifthNumeral
                            varText.set(eleventhSub)
                    if fourthMathSign == "/":
                            eleventhDiv = tenthDiv / fifthNumeral
                            varText.set(eleventhDiv)
                    if fourthMathSign == "*":
                            eleventhMulti = tenthDiv * fifthNumeral
                            varText.set(eleventhMulti)

                if thirdMathSign == '*':
                    tenthMulti = firstAdd * secondMulti
                    if fourthMathSign == "+":
                            eleventhAdd = tenthMulti + fifthNumeral
                            varText.set(eleventhAdd)
                    if fourthMathSign == "-":
                            eleventhSub = tenthMulti - fifthNumeral
                            varText.set(eleventhSub)
                    if fourthMathSign == "/":
                            eleventhDiv = tenthMulti / fifthNumeral
                            varText.set(eleventhDiv)
                    if fourthMathSign == "*":
                            eleventhMulti = tenthMulti * fifthNumeral
                            varText.set(eleventhMulti)
                            
        if firstMathSign == '-':
            twevlthZSub = firstNumeral - secondNumeral
            if secondMathSign == '+':
                twevlthaAdd = thirdNumeral + fourthNumeral
                if thirdMathSign == '+':
                    thirtenthAdd = twevlthZSub + twevlthaAdd
                    if fourthMathSign == "+":
                            fourtenthAdd = thirtenthAdd + fifthNumeral
                            varText.set(fourtenthAdd)
                    if fourthMathSign == "-":
                            fourtenthSub = thirtenthAdd - fifthNumeral
                            varText.set(fourtenthSub)
                    if fourthMathSign == "/":
                            fourtenthDiv = thirtenthAdd / fifthNumeral
                            varText.set(fourtenthDiv)
                    if fourthMathSign == "*":
                            fourtenthAdd = thirtenthAdd * fifthNumeral
                            varText.set(fourtenthAdd)
                if thirdMathSign == '-':
                    thirtenthSub = twevlthZSub - twevlthaAdd
                    if fourthMathSign == "+":
                            fourtenthAdd = thirtenthSub + fifthNumeral
                            varText.set(fourtenthAdd)
                    if fourthMathSign == "-":
                            fourtenthSub = thirtenthSub - fifthNumeral
                            varText.set(fourtenthSub)
                    if fourthMathSign == "/":
                            fourtenthDiv = thirtenthSub / fifthNumeral
                            varText.set(fourtenthDiv)
                    if fourthMathSign == "*":
                            fourtenthMulti = thirtenthSub * fifthNumeral
                            varText.set(fourtenthMulti)
                if thirdMathSign == '/':
                    thirtenthDiv = twevlthZSub / twevlthaAdd
                    if fourthMathSign == "+":
                            fourtenthAdd = thirtenthDiv + fifthNumeral
                            varText.set(fourtenthAdd)
                    if fourthMathSign == "-":
                            fourtenthSub = thirtenthDiv - fifthNumeral
                            varText.set(fourtenthSub)
                    if fourthMathSign == "/":
                            fourtenthDiv = thirtenthDiv / fifthNumeral
                            varText.set(fourtenthDiv)
                    if fourthMathSign == "*":
                            fourtenthMulti = thirtenthDiv * fifthNumeral
                            varText.set(fourtenthMulti)
                if thirdMathSign == '*':
                    thirtenthMulti = twevlthZSub * twevlthaAdd
                    if fourthMathSign == "+":
                            fourtenthAdd = thirtenthMulti + fifthNumeral
                            varText.set(fourtenthAdd)
                    if fourthMathSign == "-":
                            fourtenthSub = thirtenthMulti - fifthNumeral
                            varText.set(fourtenthSub)
                    if fourthMathSign == "/":
                            fourtenthDiv = thirtenthMulti / fifthNumeral
                            varText.set(fourtenthDiv)
                    if fourthMathSign == "*":
                            fourtenthMulti = thirtenthMulti * fifthNumeral
                            varText.set(fourtenthMulti)
            if secondMathSign == '-':
                twevlthaSub = thirdNumeral - fourthNumeral
                if thirdMathSign == '+':
                    sixtenthAdd = twevlthZSub + twevlthaSub
                    if fourthMathSign == "+":
                            sevententhAdd = sixtenthAdd + fifthNumeral
                            varText.set(sevententhAdd)
                    if fourthMathSign == "-":
                            sevententhSub = sixtenthAdd - fifthNumeral
                            varText.set(sevententhSub)
                    if fourthMathSign == "/":
                            sevententhDiv = sixtenthAdd / fifthNumeral
                            varText.set(sevententhDiv)
                    if fourthMathSign == "*":
                            sevententhMulti = sixtenthAdd * fifthNumeral
                            varText.set(sevententhMulti)
                if thirdMathSign == '-':
                    sixtenthSub = twevlthZSub - twevlthaSub
                    if fourthMathSign == "+":
                            sevententhAdd = sixtenthSub + fifthNumeral
                            varText.set(sevententhAdd)
                    if fourthMathSign == "-":
                            sevententhSub = sixtenthSub - fifthNumeral
                            varText.set(sevententhSub)
                    if fourthMathSign == "/":
                            sevententhDiv = sixtenthSub / fifthNumeral
                            varText.set(sevententhDiv)
                    if fourthMathSign == "*":
                            sevententhMulti = sixtenthSub * fifthNumeral
                            varText.set(sevententhMulti)
                if thirdMathSign == '/':
                    sixtenthDiv = twevlthZSub / twevlthaSub
                    if fourthMathSign == "+":
                            sevententhAdd = sixtenthDiv + fifthNumeral
                            varText.set(sevententhAdd)
                    if fourthMathSign == "-":
                            sevententhSub = sixtenthDiv - fifthNumeral
                            varText.set(sevententhSub)
                    if fourthMathSign == "/":
                            sevententhDiv = sixtenthDiv / fifthNumeral
                            varText.set(sevententhDiv)
                    if fourthMathSign == "*":
                            sevententhMulti = sixtenthDiv * fifthNumeral
                            varText.set(sevententhMulti)
                if thirdMathSign == '*':
                    sixtenthMulti = twevlthZSub * twevlthaSub
                    if fourthMathSign == "+":
                            sevententhAdd = sixtenthMulti + fifthNumeral
                            varText.set(sevententhAdd)
                    if fourthMathSign == "-":
                            sevententhSub = sixtenthMulti - fifthNumeral
                            varText.set(sevententhSub)
                    if fourthMathSign == "/":
                            sevententhDiv = sixtenthMulti / fifthNumeral
                            varText.set(sevententhDiv)
                    if fourthMathSign == "*":
                            sevententhMulti = sixtenthMulti * fifthNumeral
                            varText.set(sevententhMulti)
            if secondMathSign == '/':
                twevlthaDiv = thirdNumeral / fourthNumeral
                if thirdMathSign == '+':
                    eightenthAdd = twevlthZSub + twevlthaDiv
                    if fourthMathSign == "+":
                            ninetenthAdd = eightenthAdd + fifthNumeral
                            varText.set(ninetenthAdd)
                    if fourthMathSign == "-":
                            ninetenthSub = eightenthAdd - fifthNumeral
                            varText.set(ninetenthSub)
                    if fourthMathSign == "/":
                            ninetenthDiv = eightenthAdd / fifthNumeral
                            varText.set(ninetenthDiv)
                    if fourthMathSign == "*":
                            ninetenthAdd = eightenthAdd * fifthNumeral
                            varText.set(ninetenthAdd)
                if thirdMathSign == '-':
                    eightenthSub = twevlthZSub - twevlthaDiv
                    if fourthMathSign == "+":
                            ninetenthAdd = eightenthSub + fifthNumeral
                            varText.set(ninetenthAdd)
                    if fourthMathSign == "-":
                            ninetenthSub = eightenthSub - fifthNumeral
                            varText.set(ninetenthSub)
                    if fourthMathSign == "/":
                            ninetenthDiv = eightenthSub / fifthNumeral
                            varText.set(ninetenthDiv)
                    if fourthMathSign == "*":
                            ninetenthMulti = eightenthSub * fifthNumeral
                            varText.set(ninetenthMulti)
                if thirdMathSign == '/':
                    eightenthDiv = twevlthZSub / twevlthaDiv
                    if fourthMathSign == "+":
                            ninetenthAdd = eightenthDiv + fifthNumeral
                            varText.set(ninetenthAdd)
                    if fourthMathSign == "-":
                            ninetenthSub = eightenthDiv - fifthNumeral
                            varText.set(ninetenthSub)
                    if fourthMathSign == "/":
                            ninetenthDiv = eightenthDiv / fifthNumeral
                            varText.set(ninetenthDiv)
                    if fourthMathSign == "*":
                            ninetenthMulti = eightenthDiv * fifthNumeral
                            varText.set(ninetenthMulti)
                if thirdMathSign == '*':
                    eightenthMulti = twevlthZSub * twevlthaDiv
                    if fourthMathSign == "+":
                            ninetenthAdd = eightenthMulti + fifthNumeral
                            varText.set(ninetenthAdd)
                    if fourthMathSign == "-":
                            ninetenthSub = eightenthMulti - fifthNumeral
                            varText.set(ninetenthSub)
                    if fourthMathSign == "/":
                            ninetenthDiv = eightenthDiv / fifthNumeral
                            varText.set(ninetenthDiv)
                    if fourthMathSign == "*":
                            ninetenthMulti = eightenthMulti * fifthNumeral
                            varText.set(ninetenthMulti)
                            
            if secondMathSign == '*':
                twevlthaMulti = thirdNumeral * fourthNumeral
                if thirdMathSign == '+':
                    twentythAdd = twevlthZSub + twevlthaMulti
                    if fourthMathSign == "+":
                            twentyfirstAdd = twentythAdd + fifthNumeral
                            varText.set(twentyfirstAdd)
                    if fourthMathSign == "-":
                            twentyfirstSub = twentythAdd - fifthNumeral
                            varText.set(twentyfirstSub)
                    if fourthMathSign == "/":
                            twentyfirstDiv = twentythAdd / fifthNumeral
                            varText.set(twentyfirstDiv)
                    if fourthMathSign == "*":
                            twentyfirstMulti = twentythAdd * fifthNumeral
                            varText.set(twentyfirstMulti)
                if thirdMathSign == '-':
                    twentythSub = twevlthZSub - twevlthaMulti
                    if fourthMathSign == "+":
                            twentyfirstAdd = twentythSub + fifthNumeral
                            varText.set(twentyfirstAdd)
                    if fourthMathSign == "-":
                            twentyfirstSub = twentythSub - fifthNumeral
                            varText.set(twentyfirstSub)
                    if fourthMathSign == "/":
                            twentyfirstDiv = twentythSub / fifthNumeral
                            varText.set(twentyfirstDiv)
                    if fourthMathSign == "*":
                            twentyfirstMulti = twentythSub * fifthNumeral
                            varText.set(twentyfirstMulti)
                if thirdMathSign == '/':
                    twentythDiv = twevlthZSub / twevlthaMulti
                    if fourthMathSign == "+":
                            twentyfirstAdd = twentythDiv + fifthNumeral
                            varText.set(twentyfirstAdd)
                    if fourthMathSign == "-":
                            twentyfirstSub = twentythDiv - fifthNumeral
                            varText.set(twentyfirstSub)
                    if fourthMathSign == "/":
                            twentyfirstDiv = twentythDiv / fifthNumeral
                            varText.set(twentyfirstDiv)
                    if fourthMathSign == "*":
                            twentyfirstMulti = twentythDiv * fifthNumeral
                            varText.set(twentyfirstMulti)
                if thirdMathSign == '*':
                    twentythMulti = twevlthZSub * twevlthaMulti
                    if fourthMathSign == "+":
                            twentyfirstAdd = twentythMulti + fifthNumeral
                            varText.set(twentyfirstAdd)
                    if fourthMathSign == "-":
                            twentyfirstSub = twentythMulti - fifthNumeral
                            varText.set(twentyfirstSub)
                    if fourthMathSign == "/":
                            twentyfirstDiv = twentythMulti / fifthNumeral
                            varText.set(twentyfirstDiv)
                    if fourthMathSign == "*":
                            twentyfirstMulti = twentythMulti * fifthNumeral
                            varText.set(twentyfirstMulti)


        if firstMathSign == '/':
            twevlthYDiv = firstNumeral / secondNumeral
            if secondMathSign == '+':
                twevlthXAdd = thirdNumeral + fourthNumeral
                if thirdMathSign == '+':
                    twentysecondAdd = twevlthYDiv + twevlthXAdd
                    if fourthMathSign == "+":
                            twentythirdAdd = twentysecondAdd + fifthNumeral
                            varText.set(twentythirdAdd)
                    if fourthMathSign == "-":
                            twentythirdSub = twentysecondAdd - fifthNumeral
                            varText.set(twentythirdSub)
                    if fourthMathSign == "/":
                            twentythirdDiv = twentysecondAdd / fifthNumeral
                            varText.set(twentythirdDiv)
                    if fourthMathSign == "*":
                            twentythirdMulti = twentysecondAdd * fifthNumeral
                            varText.set(twentythirdMulti)
                if thirdMathSign == '-':
                    twentysecondSub = twevlthYDiv - twevlthXAdd
                    if fourthMathSign == "+":
                            twentythirdAdd = twentysecondSub + fifthNumeral
                            varText.set(twentythirdAdd)
                    if fourthMathSign == "-":
                            twentythirdSub = twentysecondSub - fifthNumeral
                            varText.set(twentythirdSub)
                    if fourthMathSign == "/":
                            twentythirdDiv = twentysecondSub / fifthNumeral
                            varText.set(twentythirdDiv)
                    if fourthMathSign == "*":
                            twentythirdMulti = twentysecondSub * fifthNumeral
                            varText.set(twentythirdMulti)
                if thirdMathSign == '/':
                    twentysecondDiv = twevlthYDiv / twevlthXAdd
                    if fourthMathSign == "+":
                            twentythirdAdd = twentysecondDiv + fifthNumeral
                            varText.set(twentythirdAdd)
                    if fourthMathSign == "-":
                            twentythirdSub = twentysecondDiv - fifthNumeral
                            varText.set(twentythirdSub)
                    if fourthMathSign == "/":
                            twentythirdDiv = twentysecondDiv / fifthNumeral
                            varText.set(twentythirdDiv)
                    if fourthMathSign == "*":
                            twentythirdMulti = twentysecondDiv * fifthNumeral
                            varText.set(twentythirdMulti)
                if thirdMathSign == '*':
                    twentysecondMulti = twevlthYDiv * twevlthXAdd
                    if fourthMathSign == "+":
                            twentythirdAdd = twentysecondMulti + fifthNumeral
                            varText.set(twentythirdAdd)
                    if fourthMathSign == "-":
                            twentythirdSub = twentysecondMulti - fifthNumeral
                            varText.set(twentythirdSub)
                    if fourthMathSign == "/":
                            twentythirdAdd = twentysecondMulti / fifthNumeral
                            varText.set(twentythirdAdd)
                    if fourthMathSign == "*":
                            twentythirdAdd = twentysecondMulti * fifthNumeral
                            varText.set(twentythirdAdd)

            if secondMathSign == '-':
                twevlthXSub = thirdNumeral - fourthNumeral
                if thirdMathSign == '+':
                    twentyfourthAdd = twevlthYDiv + twevlthXSub
                    if fourthMathSign == "+":
                            twentyfifthAdd = twentyfourthAdd + fifthNumeral
                            varText.set(twentyfifthAdd)
                    if fourthMathSign == "-":
                            twentyfifthSub = twentyfourthAdd - fifthNumeral
                            varText.set(twentyfifthSub)
                    if fourthMathSign == "/":
                            twentyfifthDiv = twentyfourthAdd / fifthNumeral
                            varText.set(twentyfifthDiv)
                    if fourthMathSign == "*":
                            twentyfifthMulti = twentyfourthAdd * fifthNumeral
                            varText.set(twentyfifthMulti)
                if thirdMathSign == '-':
                    twentyfourthSub = twevlthYDiv - twevlthXSub
                    if fourthMathSign == "+":
                            twentyfifthAdd = twentyfourthSub + fifthNumeral
                            varText.set(twentyfifthAdd)
                    if fourthMathSign == "-":
                            twentyfifthSub = twentyfourthSub - fifthNumeral
                            varText.set(twentyfifthSub)
                    if fourthMathSign == "/":
                            twentyfifthDiv = twentyfourthSub / fifthNumeral
                            varText.set(twentyfifthDiv)
                    if fourthMathSign == "*":
                            twentyfifthMulti = twentyfourthSub * fifthNumeral
                            varText.set(twentyfifthMulti)
                if thirdMathSign == '/':
                    twentyfourthDiv = twevlthYDiv / twevlthXSub
                    if fourthMathSign == "+":
                            twentyfifthAdd = twentyfourthDiv + fifthNumeral
                            varText.set(twentyfifthAdd)
                    if fourthMathSign == "-":
                            twentyfifthSub = twentyfourthDiv - fifthNumeral
                            varText.set(twentyfifthSub)
                    if fourthMathSign == "/":
                            twentyfifthDiv = twentyfourthDiv / fifthNumeral
                            varText.set(twentyfifthDiv)
                    if fourthMathSign == "*":
                            twentyfifthMulti = twentyfourthDiv * fifthNumeral
                            varText.set(twentyfifthMulti)
                if thirdMathSign == '*':
                    twentyfourthMulti = twevlthYDiv * twevlthXSub
                    if fourthMathSign == "+":
                            twentyfifthAdd = twentyfourthMulti + fifthNumeral
                            varText.set(twentyfifthAdd)
                    if fourthMathSign == "-":
                            twentyfifthSub = twentyfourthMulti - fifthNumeral
                            varText.set(twentyfifthSub)
                    if fourthMathSign == "/":
                            twentyfifthDiv = twentyfourthMulti / fifthNumeral
                            varText.set(twentyfifthDiv)
                    if fourthMathSign == "*":
                            twentyfifthMulti = twentyfourthMulti * fifthNumeral
                            varText.set(twentyfifthMulti)

            if secondMathSign == '/':
                twentyfourthDivA = thirdNumeral / fourthNumeral
                if thirdMathSign == '+':
                    twentysixthAdd = twevlthYDiv + twentyfourthDivA
                    if fourthMathSign == "+":
                            twentyseventhAdd = twentysixthAdd + fifthNumeral
                            varText.set(twentyseventhAdd)
                    if fourthMathSign == "-":
                            twentyseventhSub = twentysixthAdd - fifthNumeral
                            varText.set(twentyseventhSub)
                    if fourthMathSign == "/":
                            twentyseventhDiv = twentysixthAdd / fifthNumeral
                            varText.set(twentyseventhDiv)
                    if fourthMathSign == "*":
                            twentyseventhMulti = twentysixthAdd * fifthNumeral
                            varText.set(twentyseventhMulti)
                if thirdMathSign == '-':
                    twentysixthSub = twevlthYDiv - twentyfourthDivA
                    if fourthMathSign == "+":
                            twentyseventhAdd = twentysixthSub + fifthNumeral
                            varText.set(twentyseventhAdd)
                    if fourthMathSign == "-":
                            twentyseventhSub = twentysixthSub - fifthNumeral
                            varText.set(twentyseventhSub)
                    if fourthMathSign == "/":
                            twentyseventhDiv = twentysixthSub / fifthNumeral
                            varText.set(twentyseventhDiv)
                    if fourthMathSign == "*":
                            twentyseventhMulti = twentysixthSub * fifthNumeral
                            varText.set(twentyseventhMulti)
                if thirdMathSign == '/':
                    twentysixthDiv = twevlthYDiv / twentyfourthDivA
                    if fourthMathSign == "+":
                            twentyseventhAdd = twentysixthDiv + fifthNumeral
                            varText.set(twentyseventhAdd)
                    if fourthMathSign == "-":
                            twentyseventhSub = twentysixthDiv - fifthNumeral
                            varText.set(twentyseventhSub)
                    if fourthMathSign == "/":
                            twentyseventhDiv = twentysixthDiv / fifthNumeral
                            varText.set(twentyseventhDiv)
                    if fourthMathSign == "*":
                            twentyseventhMulti = twentysixthDiv * fifthNumeral
                            varText.set(twentyseventhMulti)
                if thirdMathSign == '*':
                    twentysixthMulti = twevlthYDiv * twentyfourthDivA
                    if fourthMathSign == "+":
                            twentyseventhAdd = twentysixthMulti + fifthNumeral
                            varText.set(twentyseventhAdd)
                    if fourthMathSign == "-":
                            twentyseventhSub = twentysixthMulti - fifthNumeral
                            varText.set(twentyseventhSub)
                    if fourthMathSign == "/":
                            twentyseventhDiv = twentysixthMulti / fifthNumeral
                            varText.set(twentyseventhDiv)
                    if fourthMathSign == "*":
                            twentyseventhMulti = twentysixthMulti * fifthNumeral
                            varText.set(twentyseventhMulti)

            if secondMathSign == '*':
                twevlthXMulti = thirdNumeral * fourthNumeral
                if thirdMathSign == '+':
                    twentyeigthAddA = twevlthYDiv + twevlthXMulti
                    if fourthMathSign == "+":
                            twentyeighthAdd = twentyeigthAddA + fifthNumeral
                            varText.set(twentyeighthAdd)
                    if fourthMathSign == "-":
                            twentyeighthSub = twentyeigthAddA - fifthNumeral
                            varText.set(twentyeighthSub)
                    if fourthMathSign == "/":
                            twentyeighthDiv = twentyeigthAddA / fifthNumeral
                            varText.set(twentyeighthDiv)
                    if fourthMathSign == "*":
                            twentyeighthMulti = twentyeigthAddA * fifthNumeral
                            varText.set(twentyeighthMulti)
                if thirdMathSign == '-':
                    twentyeigthSubA = twevlthYDiv - twevlthXMulti
                    if fourthMathSign == "+":
                            twentyeighthAdd = twentyeigthSubA + fifthNumeral
                            varText.set(twentyeighthAdd)
                    if fourthMathSign == "-":
                            twentyeighthSub = twentyeigthSubA - fifthNumeral
                            varText.set(twentyeighthSub)
                    if fourthMathSign == "/":
                            twentyeighthDiv = twentyeigthSubA / fifthNumeral
                            varText.set(twentyeighthDiv)
                    if fourthMathSign == "*":
                            twentyeighthMulti = twentyeigthSubA * fifthNumeral
                            varText.set(twentyeighthMulti)
                if thirdMathSign == '/':
                    twentyeigthDivA = twevlthYDiv / twevlthXMulti
                    if fourthMathSign == "+":
                            twentyeighthAdd = twentyeigthDivA + fifthNumeral
                            varText.set(twentyeighthAdd)
                    if fourthMathSign == "-":
                            twentyeighthSub = twentyeigthDivA - fifthNumeral
                            varText.set(twentyeighthSub)
                    if fourthMathSign == "/":
                            twentyeighthDiv = twentyeigthDivA / fifthNumeral
                            varText.set(twentyeighthDiv)
                    if fourthMathSign == "*":
                            twentyeighthMulti = twentyeigthDivA * fifthNumeral
                            varText.set(twentyeighthMulti)
                if thirdMathSign == '*':
                    twentyeigthMultiA = twevlthYDiv * twevlthXMulti
                    if fourthMathSign == "+":
                            twentyeighthAdd = twentyeigthMultiA + fifthNumeral
                            varText.set(twentyeighthAdd)
                    if fourthMathSign == "-":
                            twentyeighthSub = twentyeigthMultiA - fifthNumeral
                            varText.set(twentyeighthSub)
                    if fourthMathSign == "/":
                            twentyeighthDiv = twentyeigthMultiA / fifthNumeral
                            varText.set(twentyeighthDiv)
                    if fourthMathSign == "*":
                            twentyeighthMulti = twentyeigthMultiA * fifthNumeral
                            varText.set(twentyeighthMulti)



        if firstMathSign == '*':
            twevlth_Multi = firstNumeral * secondNumeral
            if secondMathSign == '+':
                twevlth_Add = thirdNumeral + fourthNumeral
                if thirdMathSign == '+':
                    twentyninthAdd = twevlth_Multi + twevlth_Add
                    if fourthMathSign == "+":
                            thirtethAdd = twentyninthAdd + fifthNumeral
                            varText.set(thirtethAdd)
                    if fourthMathSign == "-":
                            thirtethSub = twentyninthAdd - fifthNumeral
                            varText.set(thirtethSub)
                    if fourthMathSign == "/":
                            thirtethDiv = twentyninthAdd / fifthNumeral
                            varText.set(thirtethDiv)
                    if fourthMathSign == "*":
                            thirtethMulti = twentyninthAdd * fifthNumeral
                            varText.set(thirtethMulti)
                if thirdMathSign == '-':
                    twentyninthSub = twevlth_Multi - twevlth_Add
                    if fourthMathSign == "+":
                            thirtethAdd = twentyninthSub + fifthNumeral
                            varText.set(thirtethAdd)
                    if fourthMathSign == "-":
                            thirtethSub = twentyninthSub - fifthNumeral
                            varText.set(thirtethSub)
                    if fourthMathSign == "/":
                            thirtethDiv = twentyninthSub / fifthNumeral
                            varText.set(thirtethDiv)
                    if fourthMathSign == "*":
                            thirtethMulti = twentyninthSub * fifthNumeral
                            varText.set(thirtethMulti)
                if thirdMathSign == '/':
                    twentyninthDiv = twevlth_Multi / twevlth_Add
                    if fourthMathSign == "+":
                            thirtethAdd = twentyninthDiv + fifthNumeral
                            varText.set(thirtethAdd)
                    if fourthMathSign == "-":
                            thirtethSub = twentyninthDiv - fifthNumeral
                            varText.set(thirtethSub)
                    if fourthMathSign == "/":
                            thirtethDiv = twentyninthDiv / fifthNumeral
                            varText.set(thirtethDiv)
                    if fourthMathSign == "*":
                            thirtethMulti = twentyninthDiv * fifthNumeral
                            varText.set(thirtethMulti)
                if thirdMathSign == '*':
                    twentyninthMulti = twevlth_Multi * twevlth_Add
                    if fourthMathSign == "+":
                            thirtethAdd = twentyninthMulti + fifthNumeral
                            varText.set(thirtethAdd)
                    if fourthMathSign == "-":
                            thirtethSub = twentyninthMulti - fifthNumeral
                            varText.set(thirtethSub)
                    if fourthMathSign == "/":
                            thirtethDiv = twentyninthMulti / fifthNumeral
                            varText.set(thirtethDiv)
                    if fourthMathSign == "*":
                            thirtethMulti = twentyninthMulti * fifthNumeral
                            varText.set(thirtethMulti)
                            
            if secondMathSign == '-':
                twevlth_Sub = thirdNumeral - fourthNumeral
                if thirdMathSign == '+':
                    thirtyfirstAdd = twevlth_Multi + twevlth_Sub
                    if fourthMathSign == "+":
                            thirtysecondAdd = thirtyfirstAdd + fifthNumeral
                            varText.set(thirtysecondAdd)
                    if fourthMathSign == "-":
                            thirtysecondSub = thirtyfirstAdd - fifthNumeral
                            varText.set(thirtysecondSub)
                    if fourthMathSign == "/":
                            thirtysecondDiv = thirtyfirstAdd / fifthNumeral
                            varText.set(thirtysecondDiv)
                    if fourthMathSign == "*":
                            thirtysecondMulti = thirtyfirstAdd * fifthNumeral
                            varText.set(thirtysecondMulti)
                if thirdMathSign == '-':
                    thirtyfirstSub = twevlth_Multi - twevlth_Sub
                    if fourthMathSign == "+":
                            thirtysecondAdd = thirtyfirstSub + fifthNumeral
                            varText.set(thirtysecondAdd)
                    if fourthMathSign == "-":
                            thirtysecondSub = thirtyfirstSub - fifthNumeral
                            varText.set(thirtysecondSub)
                    if fourthMathSign == "/":
                            thirtysecondDiv = thirtyfirstSub / fifthNumeral
                            varText.set(thirtysecondDiv)
                    if fourthMathSign == "*":
                            thirtysecondMulti = thirtyfirstSub * fifthNumeral
                            varText.set(thirtysecondMulti)
                if thirdMathSign == '/':
                    thirtyfirstDiv = twevlth_Multi / twevlth_Sub
                    if fourthMathSign == "+":
                            thirtysecondAdd = thirtyfirstDiv + fifthNumeral
                            varText.set(thirtysecondAdd)
                    if fourthMathSign == "-":
                            thirtysecondSub = thirtyfirstDiv - fifthNumeral
                            varText.set(thirtysecondSub)
                    if fourthMathSign == "/":
                            thirtysecondDiv = thirtyfirstDiv / fifthNumeral
                            varText.set(thirtysecondDiv)
                    if fourthMathSign == "*":
                            thirtysecondMulti = thirtyfirstDiv * fifthNumeral
                            varText.set(thirtysecondMulti)
                if thirdMathSign == '*':
                    thirtyfirstMulti = twevlth_Multi * twevlth_Sub
                    if fourthMathSign == "+":
                            thirtysecondAdd = thirtyfirstMulti + fifthNumeral
                            varText.set(thirtysecondAdd)
                    if fourthMathSign == "-":
                            thirtysecondSub = thirtyfirstMulti - fifthNumeral
                            varText.set(thirtysecondSub)
                    if fourthMathSign == "/":
                            thirtysecondDiv = thirtyfirstMulti / fifthNumeral
                            varText.set(thirtysecondDiv)
                    if fourthMathSign == "*":
                            thirtysecondMulti = thirtyfirstMulti * fifthNumeral
                            varText.set(thirtysecondMulti)


            if secondMathSign == '/':
                twevlth_Div = thirdNumeral / fourthNumeral
                if thirdMathSign == '+':
                    thritythirdAdd = twevlth_Multi + twevlth_Div
                    if fourthMathSign == "+":
                            thirtyfourthAdd = thritythirdAdd + fifthNumeral
                            varText.set(thirtyfourthAdd)
                    if fourthMathSign == "-":
                            thirtyfourthSub = thritythirdAdd - fifthNumeral
                            varText.set(thirtyfourthSub)
                    if fourthMathSign == "/":
                            thirtyfourthDiv = thritythirdAdd / fifthNumeral
                            varText.set(thirtyfourthDiv)
                    if fourthMathSign == "*":
                            thirtyfourthMulti = thritythirdAdd * fifthNumeral
                            varText.set(thirtyfourthMulti)
                if thirdMathSign == '-':
                    thritythirdSub = twevlth_Multi - twevlth_Div
                    if fourthMathSign == "+":
                            thirtyfourthAdd = thritythirdSub + fifthNumeral
                            varText.set(thirtyfourthAdd)
                    if fourthMathSign == "-":
                            thirtyfourthSub = thritythirdSub - fifthNumeral
                            varText.set(thirtyfourthSub)
                    if fourthMathSign == "/":
                            thirtyfourthDiv = thritythirdSub / fifthNumeral
                            varText.set(thirtyfourthDiv)
                    if fourthMathSign == "*":
                            thirtyfourthMulti = thritythirdSub * fifthNumeral
                            varText.set(thirtyfourthMulti)
                if thirdMathSign == '/':
                    thritythirdDiv = twevlth_Multi / twevlth_Div
                    if fourthMathSign == "+":
                            thirtyfourthAdd = thritythirdDiv + fifthNumeral
                            varText.set(thirtyfourthAdd)
                    if fourthMathSign == "-":
                            thirtyfourthSub = thritythirdDiv - fifthNumeral
                            varText.set(thirtyfourthSub)
                    if fourthMathSign == "/":
                            thirtyfourthDiv = thritythirdDiv / fifthNumeral
                            varText.set(thirtyfourthDiv)
                    if fourthMathSign == "*":
                            thirtyfourthMulti = thritythirdDiv * fifthNumeral
                            varText.set(thirtyfourthMulti)
                if thirdMathSign == '*':
                    thritythirdMulti = twevlth_Multi * twevlth_Div
                    if fourthMathSign == "+":
                            thirtyfourthAdd = thritythirdMulti + fifthNumeral
                            varText.set(thirtyfourthAdd)
                    if fourthMathSign == "-":
                            thirtyfourthSub = thritythirdMulti - fifthNumeral
                            varText.set(thirtyfourthSub)
                    if fourthMathSign == "/":
                            thirtyfourthDiv = thritythirdMulti / fifthNumeral
                            varText.set(thirtyfourthDiv)
                    if fourthMathSign == "*":
                            thirtyfourthMulti = thritythirdMulti * fifthNumeral
                            varText.set(thirtyfourthMulti)


            if secondMathSign == '*':
                twevlthMulti_ = thirdNumeral * fourthNumeral
                if thirdMathSign == '+':
                    thirtyfifthAdd = twevlth_Multi + twevlthMulti_
                    if fourthMathSign == "+":
                            thirtysixthAdd = thirtyfifthAdd + fifthNumeral
                            varText.set(thirtysixthAdd)
                    if fourthMathSign == "-":
                            thirtysixthSub = thirtyfifthAdd - fifthNumeral
                            varText.set(thirtysixthSub)
                    if fourthMathSign == "/":
                            thirtysixthDiv = thirtyfifthAdd / fifthNumeral
                            varText.set(thirtysixthDiv)
                    if fourthMathSign == "*":
                            thirtysixthMulti = thirtyfifthAdd * fifthNumeral
                            varText.set(thirtysixthMulti)

                if thirdMathSign == '-':
                    thirtyfifthSub = twevlth_Multi - twevlthMulti_
                    if fourthMathSign == "+":
                            thirtysixthAdd = thirtyfifthSub + fifthNumeral
                            varText.set(thirtysixthAdd)
                    if fourthMathSign == "-":
                            thirtysixthSub = thirtyfifthSub - fifthNumeral
                            varText.set(thirtysixthSub)
                    if fourthMathSign == "/":
                            thirtysixthDiv = thirtyfifthSub / fifthNumeral
                            varText.set(thirtysixthDiv)
                    if fourthMathSign == "*":
                            thirtysixthMulti = thirtyfifthSub * fifthNumeral
                            varText.set(thirtysixthMulti)

                if thirdMathSign == '/':
                    thirtyfifthDiv = twevlth_Multi / twevlthMulti_
                    if fourthMathSign == "+":
                            thirtysixthAdd = thirtyfifthDiv + fifthNumeral
                            varText.set(thirtysixthAdd)
                    if fourthMathSign == "-":
                            thirtysixthSub = thirtyfifthDiv - fifthNumeral
                            varText.set(thirtysixthSub)
                    if fourthMathSign == "/":
                            thirtysixthDiv = thirtyfifthDiv / fifthNumeral
                            varText.set(thirtysixthDiv)
                    if fourthMathSign == "*":
                            thirtysixthMulti = thirtyfifthDiv * fifthNumeral
                            varText.set(thirtysixthMulti)

                if thirdMathSign == '*':
                    thirtyfifthMulti = twevlth_Multi * twevlthMulti_
                    if fourthMathSign == "+":
                            thirtysixthAdd = thirtyfifthMulti + fifthNumeral
                            varText.set(thirtysixthAdd)
                    if fourthMathSign == "-":
                            thirtysixthSub = thirtyfifthMulti - fifthNumeral
                            varText.set(thirtysixthSub)
                    if fourthMathSign == "/":
                            thirtysixthAdd = thirtyfifthMulti / fifthNumeral
                            varText.set(thirtysixthAdd)
                    if fourthMathSign == "*":
                            thirtysixthMulti = thirtyfifthMulti * fifthNumeral
                            varText.set(thirtysixthMulti)
        return

updateT_text = Button(App, width=8, command=algebraAdd, text="Calculate")
updateT_text.grid(row=19, column=0)
varText = IntVar()
updated_text = Entry(App, textvariable=varText)
updated_text.grid(row=20, column=0)

App.mainloop

