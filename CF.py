from tkinter import*
Wind = Tk()
Wind.geometry("400x200")
Wind.title("Celsius to Fahrenheit Converter")
Wind.configure(background = "light grey")

def Convert(): 
   fans = float(enter.get()) * 1.8 + 32
   fahans.config(text = fans)


weight = Label(Wind,text = "Enter weight in Celsius :",background = "light grey",fg = "black")
enter = Entry(Wind,background="white",fg = "black",width = 20)
convert = Button(Wind,text = "Convert",background = "light green",fg = "black", command = Convert)
fahrenheit = Label(Wind,text = "Temperature in Fahrenheit :",background = "light grey",fg = "black")
fahans = Label(Wind,background = "light grey",fg = "black")

weight.place(x = 20, y = 20)
enter.place(x = 160,y = 20)
convert.place(x = 50,y = 120)
fahrenheit.place(x = 20, y = 80)
fahans.place(x=180,y=80)

Wind.mainloop()