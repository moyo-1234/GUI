from tkinter import*
Wind = Tk()

scrollbar = Scrollbar(Wind)
scrollbar.pack(side = RIGHT,fill = Y)
listbox = Listbox(Wind,height=10,width=20,bg="black",fg="white",yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
listbox.insert(1,"Winter")
listbox.insert(2,"Spring")
listbox.insert(3,"Summmer")
listbox.insert(4,"Autumn")

for i in range(50):
    listbox.insert(END,"Season"+ str(i))






listbox.pack()
Wind.mainloop()