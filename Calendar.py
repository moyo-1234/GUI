from tkinter import*
Wind = Tk()
Wind.title("Main")
import calendar
def display():
    Cale = Tk()
    Cale.title("Calendar")
    Cale.configure(background = "light green")
    Cale.geometry("550x600")
    yc = int(year.get())
    calen = calendar.calendar(yc)
    Calendar = Label(Cale,text = calen,bg = "light green",fg = "black")
    Calendar.pack()



cal = Label(Wind,text = "CALENDAR",background = "grey",fg = "black",font = ("Times New Roman", 25, "bold"))
enter = Label(Wind,text = "Enter Year",background = "light green",fg = "black")
year = Entry(Wind,background = "white",fg = "black",width = 20)
show = Button(Wind,text="Show Calendar",background = "Red",fg="black",command = display)
exit = Button(Wind,text="Exit",background = "Red",fg="black",command=Wind.destroy)

cal.pack()
enter.pack()
year.pack()
show.pack()
exit.pack()








Wind.mainloop()
