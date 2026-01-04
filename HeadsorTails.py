from tkinter import*
import random
from tkinter import messagebox
Wind = Tk()
Wind.geometry("300x150")
Wind.title("Heads or Tails")
Wind.configure(background = "light grey")

def Auto():
    Rn = random.randint(1,2)
    check = int(Tans.get())
    if Rn == check:
        messagebox.showinfo("Win","Your number is correct")
    else:
        messagebox.showinfo("Loss","The answer was the other number")

Guess = Label(Wind,text = "Guess whether it is 1 or 2",background = "light grey",fg = "black")
FulGue = Button(Wind,text="Guess",background = "light grey",fg="white",command = Auto)
Tans = Entry(Wind,background="white",fg = "black",width = 20)



Guess.place(x=60,y=40)
FulGue.place(x=200,y=60)
Tans.place(x=60,y=65)

Wind.mainloop()