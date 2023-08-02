import tkinter
from tkinter import *

expression=""

def press(num):

    global expression

    expression = expression + str(num)
    equation.set(expression)



def equalpress():


    try:
        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""

    except:
        equation.set(" ERROR ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__=="__main__":
    window = Tk()
    window.geometry("1000x1000")

    equation = StringVar()

    expression_field = Entry(window,textvariable=equation,bg="black",fg="blue")
    expression_field.grid(columnspan=4, ipadx=70)

    window.title("Calculator")
    window.configure(bg="black")

    button1 = Button(window, text="1", fg="blue", bg="white", command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(window, text="2", fg="blue", bg="white", command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(window, text="3", fg="blue", bg="white", command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(window, text="4", fg="blue", bg="white", command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(window, text="5", fg="blue", bg="white", command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(window, text="6", fg="blue", bg="white", command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(window, text="7", fg="blue", bg="white", command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(window, text="8", fg="blue", bg="white", command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(window, text="9", fg="blue", bg="white", command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(window, text="0", fg="blue", bg="white", command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=1)

    plus = Button(window, text="+", fg="white", bg="#7eb7ed", command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(window, text="-", fg="white", bg="#7eb7ed", command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(window, text="X", fg="white", bg="#7eb7ed", command=lambda: press("X"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(window, text="/", fg="white", bg="#7eb7ed", command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    percentage = Button(window, text="%", fg="white", bg="#7eb7ed", command=lambda: press("%"), height=1, width=7)
    percentage.grid(row=6, column=3)

    equalto = Button(window, text="=", fg="white", bg="blue", command=equalpress, height=1, width=28)
    equalto.grid(row=6, columnspan=3)

    dot = Button(window, text=".", fg="blue", bg="white", command=lambda: press("."), height=1, width=7)
    dot.grid(row=5, column=0)

    clear = Button(window, text="C", fg="blue", bg="white", command=clear, height=1, width=7)
    clear.grid(row=5, column=2)

    window.mainloop()


