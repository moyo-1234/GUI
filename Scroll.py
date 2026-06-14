import tkinter
from tkinter import*
root = tkinter.Tk()
root.geometry("500x500")


Save = Button(root,text = "SAVE")
Save.place(x=50,y=25)
Open = Button(root, text = "OPEN")
Open.place(x=90,y=25)
Delete = Button(root, text = "DELETE")
Delete.place(x=135,y=25)
add = Button(root,text = "ADD")
add.place(x=200,y=150)
deb = Entry(root)
deb.place(x=200,y=90)
bar = Scrollbar(root)
bar.pack(side = RIGHT,fill=Y)
contain = Listbox(root,height=20,width = 30,bg = "blue", fg ="white",yscrollcommand=bar.set)
contain.place(x=10,y=90)







root.mainloop()
