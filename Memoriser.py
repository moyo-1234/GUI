import tkinter
from tkinter import*
from tkinter.filedialog import*
root = tkinter.Tk()
root.geometry("500x500")

def av():
    text = deb.get()
    contain.insert(END,text)
    deb.delete(0,END)

def dv():
    index = contain.curselection()
    contain.delete(index)

def sv():
    fina = asksaveasfile(defaultextension=".txt")
    for i in contain.get(0,END):
        print(i.strip(),file=fina)
    contain.delete(0,END)

def ov():
    title = askopenfile(title = "Memoriser") 
    contain.delete(0,END)
    lines = title.readlines()
    for i in lines:
        contain.insert(END,i)

Save = Button(root,text = "SAVE",command = sv)
Save.place(x=50,y=25)
Open = Button(root, text = "OPEN",command = ov)
Open.place(x=90,y=25)
Delete = Button(root, text = "DELETE",command = dv)
Delete.place(x=135,y=25)
add = Button(root,text = "ADD",command = av)
add.place(x=200,y=150)
deb = Entry(root)
deb.place(x=200,y=90)
bar = Scrollbar(root)
bar.pack(side = RIGHT,fill=Y)
contain = Listbox(root,height=20,width = 30,bg = "blue", fg ="white",yscrollcommand=bar.set)
contain.place(x=10,y=90)






root.mainloop()
