import tkinter
from tkinter import *

window=Tk()
window.geometry("500x500")
window.title("Calculator")
window.configure(bg="#0ee68c")

button1 = Button(window,text="1",fg="black",bg="white",command=lambda : press(1),height=1,width=7)
button1.grid(row=2,column=0)

button2 = Button(window,text=2,fg="black",bg="white",command=lambda :press(2),height=1,width=7)
button2.grid(row=2,column=1)

button3 = Button(window,text="3",fg="black",bg="white",command=lambda :press(3),height=1,width=7)
button3.grid(row=2,column=2)

button4 = Button(window,text="4",fg="black",bg="white",command=lambda :press(4),height=1,width=7)
button4.grid(row=3,column=0)

button5 = Button(window,text="5",fg="black",bg="white",command=lambda :press(5),height=1,width=7)
button5.grid(row=3,column=1)

button6 = Button(window,text="6",fg="black",bg="white",command=lambda :press(6),height=1,width=7)
button6.grid(row=3,column=2)

button7 = Button(window,text="7",fg="black",bg="white",command=lambda :press(7),height=1,width=7)
button7.grid(row=4,column=0)

button8 = Button(window,text="8",fg="black",bg="white",command=lambda :press(8),height=1,width=7)
button8.grid(row=4,column=1)

button9 = Button(window,text="9",fg="black",bg="white",command=lambda :press(9),height=1,width=7)
button9.grid(row=4,column=2)

button0 = Button(window,text="0",fg="black",bg="white",command=lambda :press(0),height=1,width=7)
button0.grid(row=5,column=0)

window.mainloop()