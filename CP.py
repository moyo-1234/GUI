from tkinter import*
import tkinter

wind = Tk()
wind.title("Control Panel")
wind.geometry("200x200")
frame = Frame(wind)
frame.pack(side = TOP)
frame2 = Frame(wind)
frame2.pack(side = BOTTOM)

Start = Button(frame,text="Start",fg = "green")
Stop = Button(frame,text="Stop",fg = "red")
Start.pack(side = LEFT)
Stop.pack(side = RIGHT)

Settings = Button(frame2,text="Settings",fg = "black")
Exit = Button(frame2,text="Exit",fg = "red")
Settings.pack(side = LEFT)
Exit.pack(side = RIGHT)

wind.mainloop()