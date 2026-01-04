from tkinter import*
Wind = Tk()
Wind.configure(background="light blue")

frame = Frame(Wind)
frame2 = Frame(Wind)


button1 = Button(frame,text="Starters",bg="light blue",fg = "black")
button2 = Button(frame,text="Mains",bg="light blue",fg = "black")
button3 = Button(frame,text="Deserts",bg="light blue",fg = "black")
buttona = Button(frame2,text = "Domino's",bg="dark blue",fg="red")
buttonb = Button(frame2,text = "Mcdonalds",bg="red",fg="yellow")
buttonc = Button(frame2,text = "KFC",bg="red",fg="white")


button3.pack(side=RIGHT)
button2.pack(side=RIGHT)
button1.pack(side=RIGHT)
buttonc.pack(side = TOP)
buttonb.pack(side = TOP)
buttona.pack(side = TOP)
frame.pack(side = LEFT)
frame2.pack(side = RIGHT)
Wind.mainloop()