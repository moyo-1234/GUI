import tkinter
from tkinter import*
from tkinter.filedialog import*
root = tkinter.Tk()
root.geometry("500x500")

lb = Frame(root)
lb.pack()

def bv():
    index = contain.curselection()
    hold = contain.get(index[0])
    root.config(bg = hold)

def av():
    text = deb.get()
    contain.insert(END,text)
    deb.delete(0,END)

def dv():
    index = contain.curselection()
    contain.delete(index)

Delete = Button(root, text = "DELETE",command = dv)
Delete.place(x=350,y=25)
add = Button(root,text = "ADD",command = av)
add.place(x=350,y=150)
bgc = Button(root,text = "BACKGROUND COLOR",command = bv)
bgc.place(x=350,y=275)
deb = Entry(root)
deb.place(x=350,y=90)
bar = Scrollbar(lb)
bar.pack(side = RIGHT,fill=Y)
contain = Listbox(lb,height=10,width = 30,bg = "blue", fg ="white",yscrollcommand=bar.set)
contain.pack()

contain.insert(END,"orange","red","black","blue")


root.mainloop()