import tkinter
from tkinter import*
import time
flag = 1
b1 = 0
b2 = 0
b3 = 0
ba = 0
bb = 0
bc = 0
bx = 0
by = 0
bz = 0
root = tkinter.Tk("900x900")
TurnLbl = Label(root, text = "")





def wincheck1():
    if b1 == "X" and b2 == "X" and b3 == "X" or ba == 1 and bb == 1 and bc == 1 or bx == 1 and by == 1 and bz == 1 or b1 == 1 and ba == 1 and bx == 1 or b2 == 1 and bb == 1 and by == 1 or b3 == 1 and bc == 1 and bz == 1 or b1 == 1 and bb == 1 and bz == 1 or b3 == 1 and bb == 1 and bx == 1:
        time.sleep(3)
        Winlbl.config(text = "Player 1 Wins")
    # elif ba == "X" and bb == "X" and bc == "X":
    #     time.sleep(3)
    #     Winlbl.config(text = "Player 1 Wins")
    # elif bx == "X" and by == "X" and bz == "X":
    #     time.sleep(3)
    #     Winlbl.config(text = "Player 1 Wins")
    # elif b1 == "X" and ba == "X" and bx == "X":
    #     time.sleep(3)
    #     Winlbl.config(text = "Player 1 Wins")
    # elif b2 == "X" and bb == "X" and by == "X":
    #     time.sleep(3)
    #     Winlbl.config(text = "Player 1 Wins")
    # elif b3 == "X" and bc == "X" and bz == "X":
    #     time.sleep(3)
    #     Winlbl.config(text = "Player 1 Wins")
    # elif b1 == "X" and bb == "X" and bz == "X":
    #     time.sleep(3)
    #     Winlbl.config(text = "Player 1 Wins")
    # elif b3 == "X" and bb == "X" and bx == "X":
    #     time.sleep(3)
    #     Winlbl.config(text = "Player 1 Wins")



def wincheck2():
    if b1 == "O" and b2 == "O"  and b3 == "O" :
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif ba == "O"  and bb == "O"  and bc == "O":
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif bx == "O"  and by == "O" and bz == "O":
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif b1 == "O"  and ba == "O" and bx == "O":
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif b2 == "O"  and bb == "O" and by == "O":
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif b3 == "O" and bc == "O" and bz == "O":
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif b1 == "O" and bb == "O" and bz == "O":
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
    elif b3 == "O" and bb == "O" and bx == "O":
        time.sleep(3)
        Winlbl.config(text = "Player 2 Wins")
        



def ttt1():
    global TurnLbl
    global flag
    global b1
    if flag == 1:
        button1.config(text = "X")
        flag = flag - 1
        b1 = b1 + 1
        TurnLbl.config(text = "X's Turn",fg = "dark red")
        wincheck1()
    elif flag == 0:
        button1.config(text = "O")
        flag = flag + 1
        b1 = b1 + 2
        TurnLbl.config(text = "O's Turn",fg = "dark blue")
        wincheck2()

def ttt2():
    global TurnLbl
    global flag
    global b2
    if flag == 1:
        button2.config(text = "X")
        flag = flag - 1
        b2 = b2 + 1
        TurnLbl.config(text = "X's Turn",fg = "dark red")
        wincheck1()
    elif flag == 0:
        button2.config(text = "O")
        flag = flag + 1
        b2 = b2 + 2
        TurnLbl.config(text = "O's Turn",fg = "dark blue")
        wincheck2()

def ttt3():
    global TurnLbl
    global flag
    global b3
    if flag == 1:
        button3.config(text = "X")
        flag = flag - 1
        b3 = b3 + 1
        TurnLbl.config(text = "X's Turn",fg = "dark red")
        wincheck1()
    elif flag == 0:
        button3.config(text = "O")
        flag = flag + 1
        b3 = b3 + 2
        TurnLbl.config(text = "O's Turn",fg = "dark blue")
        wincheck2()

def tttA():
    global TurnLbl
    global flag
    global ba
    if flag == 1:
        buttona.config(text = "X")
        flag = flag - 1
        ba = ba + 1
        TurnLbl.config(text = "X's Turn",fg = "dark red")
        wincheck1()
    elif flag == 0:
        buttona.config(text = "O")
        flag = flag + 1
        ba = ba + 1
        TurnLbl.config(text = "O's Turn",fg = "dark blue")
        wincheck2()

def tttB():
    global TurnLbl
    global flag
    global bb
    if flag == 1:
        buttonb.config(text = "X")
        flag = flag - 1
        bb = bb + 1
        TurnLbl.config(text = "X's Turn",fg = "dark red")
        wincheck1()
    elif flag == 0:
        buttonb.config(text = "O")
        flag = flag + 1
        bb = bb + 2
        TurnLbl.config(text = "O's Turn",fg = "dark blue")
        wincheck2()

def tttC():
    global TurnLbl
    global flag
    global bc
    if flag == 1:
        buttonc.config(text = "X")
        flag = flag - 1
        bc = bc + 1
        TurnLbl.config(text = "X's Turn",fg = "dark red")
        wincheck1()
    elif flag == 0:
        buttonc.config(text = "O")
        flag = flag + 1
        bc = bc + 2
        TurnLbl.config(text = "O's Turn",fg = "dark blue")
        wincheck2()

def tttX():
    global TurnLbl
    global flag
    global bx
    if flag == 1:
        buttonx.config(text = "X")
        flag = flag - 1
        bx = bx + 1
        TurnLbl.config(text = "X's Turn",fg = "dark red")
        wincheck1()
    elif flag == 0:
        buttonx.config(text = "O")
        flag = flag + 1
        bx = bx + 2
        TurnLbl.config(text = "O's Turn",fg = "dark blue")
        wincheck2()


def tttY():
    global TurnLbl
    global flag
    global by
    if flag == 1:
        buttony.config(text = "X")
        flag = flag - 1
        by = by + 1
        TurnLbl.config(text = "X's Turn",fg = "dark red")
        wincheck1()
    elif flag == 0:
        buttony.config(text = "O")
        flag = flag + 1
        by = by + 2
        TurnLbl.config(text = "O's Turn",fg = "dark blue")
        wincheck2()


def tttZ():
    global TurnLbl
    global flag
    global bz
    if flag == 1:
        buttonz.config(text = "X")
        flag = flag - 1
        bz = bz + 1
        TurnLbl.config(text = "X's Turn",fg = "dark red")
        wincheck1()
    elif flag == 0:
        buttonz.config(text = "O")
        flag = flag + 1
        bz = bz + 2
        TurnLbl.config(text = "O's Turn",fg = "dark blue")
        wincheck2()

button1 = Button(root,command = ttt1,text = "")
button2 = Button(root,command = ttt2, text="")
button3 = Button(root,command = ttt3, text = "")
buttona = Button(root,command = tttA,text = "")
buttonb = Button(root,command = tttB, text = "")
buttonc = Button(root,command = tttC, text = "")
buttonx = Button(root,command = tttX, text = "")
buttony = Button(root,command = tttY, text = "")
buttonz = Button(root,command = tttZ, text = "")
Winlbl = Label(root,text = "",fg = "gold")






        


button1.grid(row = 0, column = 0,padx = 10, pady = 10)
button2.grid(row = 0, column = 3,padx = 10, pady = 10)
button3.grid(row = 0, column = 6,padx = 10, pady = 10)
buttona.grid(row = 3, column = 0,padx = 10, pady = 10)
buttonb.grid(row = 3, column = 3,padx = 10, pady = 10)
buttonc.grid(row = 3, column = 6,padx = 10, pady = 10)
buttonx.grid(row = 6, column = 0,padx = 10, pady = 10)
buttony.grid(row = 6, column = 3,padx = 10, pady = 10)
buttonz.grid(row = 6, column = 6,padx = 10, pady = 10)
Winlbl.place(x = 130, y = 50)
TurnLbl.place(x = 130, y = 20)

root.mainloop()