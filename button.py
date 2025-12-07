from tkinter import*
Wind = Tk()

button = Button(Wind,text="text",background = "Red",fg="white",command=Wind.destroy)
label = Label(Wind,text = "Hello",background = "Red",fg = "black")
entry = Entry(Wind,background = "Blue",fg = "black",width = 5)
button.pack()
label.pack()
entry.pack()





Wind.mainloop()
