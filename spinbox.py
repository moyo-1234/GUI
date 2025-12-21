from tkinter import*
from tkinter.ttk import*
import time
Wind = Tk()
def anima():
    progress["value"] = 20
    Wind.update_idletasks()
    time.sleep(1)
    progress["value"] = 40
    Wind.update_idletasks()
    time.sleep(1)
    progress["value"] = 60
    Wind.update_idletasks()
    time.sleep(1)
    progress["value"] = 80
    Wind.update_idletasks()
    time.sleep(1)
    progress["value"] = 100
    Wind.update_idletasks()
    time.sleep(1)



spin=Spinbox(Wind,from_=1,to=10)
spin.pack()
progress = Progressbar(Wind,orient = HORIZONTAL,length=100)
progress.pack()
anim = Button(Wind,text = "Start",command = anima)
anim.pack()



Wind.mainloop()