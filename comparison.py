from tkinter import*
Wind = Tk()
Wind.geometry("300x150")
Wind.title("tk")
Wind.configure(background = "light grey")

def Convert():
   gans = float(enter.get()) * 1000  
   pans = float(enter.get()) * 2.2046
   Oans = float(enter.get()) * 35.274
   gramans.config(text = gans)
   lbsans.config(text = pans)
   Ozans.config(text = Oans)



weight = Label(Wind,text = "Enter weight in Kg",background = "light grey",fg = "black")
enter = Entry(Wind,background="white",fg = "black",width = 20)
convert = Button(Wind,text = "Convert",background = "light grey",fg = "black", command = Convert)
gram = Label(Wind,text = "Grams",background = "light grey",fg = "black")
gramans = Label(Wind,background = "white",fg = "black")
pound = Label(Wind,text = "Pounds",background = "light grey",fg = "black")
lbsans = Label(Wind,background = "white",fg = "black")
ounce = Label(Wind,text = "Ounces",background = "light grey",fg = "black")
Ozans = Label(Wind,background = "white",fg = "black")










weight.place(x = 20, y = 20)
enter.place(x = 150,y = 20)
convert.place(x = 330,y = 20)
gram.place(x = 20, y = 50)
pound.place(x = 120, y = 50)
ounce.place(x = 220,y = 50)
gramans.place(x = 20,y = 65)
lbsans.place(x=120,y = 65 )
Ozans.place(x = 220, y = 65)


Wind.mainloop()