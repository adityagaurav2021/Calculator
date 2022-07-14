from tkinter import *
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvslue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()


root.geometry("650x1200")
root.minsize(649, 1999)
root.maxsize(651, 2001)

root.title("Calculator code by Aditya Gaurav")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root, borderwidth=18, textvariable=scvalue, font="lucida 40 bold", relief=SUNKEN)
screen.pack(fill=X, ipadx=8, padx=10, pady=10)
f = Frame(root, borderwidth=18,  bg="Sky blue", relief=SUNKEN)
f.pack()
f1 = Frame(root, borderwidth=18, bg="Sky blue", relief=SUNKEN)
f1.pack()
f2 = Frame(root, borderwidth=18, bg="Sky blue", relief=SUNKEN)
f2.pack()
f3 = Frame(root, borderwidth=18, bg="Sky blue", relief=SUNKEN)
f3.pack()
f4 = Frame(root, borderwidth=18, bg="Sky blue", relief=SUNKEN)
f4.pack()
f5 = Frame(root,borderwidth=18, bg="Sky blue", relief=SUNKEN)
f5.pack()




b = Button(f, text="9", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f, text="8", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f, text="7", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f1, text="6", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="5", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f1, text="4", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f2, text="3", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f2, text="2", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f2, text="1", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f3, text="0", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)


b = Button(f3, text="+", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f3, text="-", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f4, text="*", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f4, text="/", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)

b = Button(f4, text="%", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f5, text="=", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)
b = Button(f5, text="c", font="lucida 25 bold")
b.pack(side="left", padx=10, pady=10)
b.bind("<Button-1>", click)











root.mainloop()
