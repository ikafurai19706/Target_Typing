# coding: utf-8
import threading as th
import hashlib, time, re, random, sys, keyboard, textwrap
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageFont, ImageDraw
import pyautogui


def DisplayPos():
    S_width = root.winfo_screenwidth()
    S_height = root.winfo_screenheight()
    W_width = S_width//2 - 320
    W_height = S_height//2 - 240
    return "640x480+"+str(W_width)+"+"+str(W_height)


def ResetScreen():
    quitB.pack_forget()
    titlestartB.pack_forget()
    startB.pack_forget()
    returnB.pack_forget()
    exitB.pack_forget()
    wordC1.delete(bg_text)
    wordC1.delete(fg_text)
    wordC1.place_forget()
    titleL.pack_forget()
    optionL1.pack_forget()
    optionL2.pack_forget()
    optionL3.pack_forget()
    optionL4.place_forget()
    countdownL.pack_forget()
    meaningL.place_forget()
    circleL.place_forget()
    qamtL.place_forget()
    booktypeRB0.place_forget()
    booktypeRB1.place_forget()
    amountE.place_forget()
    optionF1.pack_forget()
    watchL.pack_forget()
    

def TitleScreen():
    ResetScreen()
    quitB.pack(side="bottom", pady=30)
    titlestartB.pack(side="bottom")
    titleL.pack(pady=100)

    
def PreGame():
    ResetScreen()
    optionL1.pack(pady=10)
    optionF1.pack(pady=5)
    optionL2.pack(pady=5)
    booktypeRB0.place(x=200, y=160, anchor="center")
    booktypeRB1.place(x=440, y=160, anchor="center")
    optionL3.pack(pady=40)
    optionL4.place(x=250, y=240,anchor="center")
    amountE.place(x=390, y=240, anchor="center")
    if amountE.get() == "":
        amountE.insert(index="end", string="10")
    startB.pack(side="right", anchor="se", padx=5, pady=5)
    returnB.pack(side="right", anchor="se", padx=5, pady=5)

def NumCheck():
    if int(amountE.get()) > 200 and booktype.get() == 0:
        amountE.delete(first=0, last="end")
        amountE.insert(index="end", string="200")
        return False
    elif int(amountE.get()) > 1900 and booktype.get() == 1:
        amountE.delete(first=0,last="end")
        amountE.insert(index="end", string="1900")
        return False

def isOk(num, diff):
    if num == "":
        amountE.delete(first=0,last="end")
        amountE.insert(index="end", string="1")
        return False
    if not re.match(re.compile("[0-9]+"), diff):
        root.bell()
        return False
    if int(num) > 200 and booktype.get() == 0:
        amountE.delete(first=0,last="end")
        amountE.insert(index="end", string="200")
        return False
    elif int(num) > 1900 and booktype.get() == 1:
        amountE.delete(first=0,last="end")
        amountE.insert(index="end", string="1900")
        return False
    return True



def StartScreen():
    if int(amountE.get()) == 0:
        root.bell()
        return
    global lines
    global w_len
    global originlines
    global tnum
    if booktype.get() == 0:
        with open("1400-test.txt", "r", encoding="utf-8") as f:
            originlines = f.readlines()
    elif booktype.get() == 1:
        with open("1900.txt", "r", encoding="utf-8") as f:
            originlines = f.readlines()
    lines = list(map(lambda s:s.rstrip("\n"), originlines))
    w_len = len(lines)
    t[tnum] = th.Thread(target=StartFunc1)
    t[tnum].setDaemon(True)
    t[tnum].start()
    tnum += 1

def StartFunc1():
    global running
    if running:return
    running = True
    global tnum
    global found
    global stop
    ResetScreen()
    countdownL.place(x=320, y=240, anchor="center")
    for i in reversed(range(1, 4)):
        countdown.set(i)
        time.sleep(1)
    countdownL.place_forget()
    t[tnum] = th.Thread(target=MainGame1)
    t[tnum].setDaemon(True)
    t[tnum].start()
    tnum += 1
    t[tnum] = th.Thread(target=MainGame2)
    t[tnum].setDaemon(True)
    t[tnum].start()
    tnum += 1
    while not stop:
        time.sleep(0.5)
    pyautogui.press("enter")
    found = True
    stop = False
    running = False


def MainGame1():
    global stop
    global bg_text
    global fg_text
    global typing
    typing = True
    qamtI.set(1)
    qamtL.place(x=0, y=240, anchor="w")
    wordC1.place(x=320,y=180, anchor="center")
    for i in random.sample(lines, w_len):
        qamtS.set(str(qamtI.get()) + "/" + str(amountE.get()))
        fg_text = wordC1.create_text(0, 0, text="")
        word_fg.set("")
        j = 0
        word_r = i.split(",")
        word_r_len = len(word_r[0])
        word_bg.set(word_r[0])
        w, h = draw.textsize(word_r[0], font)
        print(w, h)
        bg_text = wordC1.create_text(320, 25, text=word_bg.get(), anchor="center", font=("MS Gothic", 20), fill="gray")
        fg_w = 320 - (w/1.7)
        meaning.set(textwrap.fill(word_r[1], 20))
        while j < word_r_len:
            t = str(keyboard.read_event())
            if stop:break
            try:
                search = re.search(pattern, t, flags=re.IGNORECASE).group()
            except AttributeError:          
                search = ""
            print(search)
            if search == word_r[0][j]:
                word_fg.set(str(word_fg.get())+word_r[0][j])
                j += 1
                wordC1.delete(fg_text)
                fg_text = wordC1.create_text(fg_w, 25, text=word_fg.get(), anchor="w", font=("MS Gothic", 20))
        if stop:break
        circleL.place(x=320, y=240, anchor="center")
        typing = False
        time.sleep(0.8)
        if qamtI.get() == int(amountE.get()):
            ForcedReturn()
            break
        circleL.place_forget()
        wordC1.delete(bg_text)
        wordC1.delete(fg_text)
        qamtI.set(qamtI.get()+1)
        typing = True
        


def MainGame2():
    global stop
    global found
    global typing
    tempTime = 0
    exitB.pack(side="bottom", anchor="se")
    meaningL.place(x=320, y=220, anchor="n")
    watchL.pack(anchor='nw')
    while not stop:
        while not typing:
            if stop:break
            time.sleep(0.1)
        startTime = time.time()
        while typing:
            if stop:break
            currentTime = time.time()
            dispTime = round(currentTime - startTime + tempTime, 2)
            watch.set(str(dispTime).ljust(len(str(int(dispTime)))+3,"0")+" sec")
        tempTime = dispTime
    watchL.pack_forget()


def ForcedReturn():
    global stop
    stop = True
    TitleScreen()

def Quit():
    sys.exit()


running = False
lines = None
w_len = None
originlines = None
pattern = "(?<=KeyboardEvent\().*(?= down\))"
search = ""
found = True
stop = False
typing = False
startflag = False
t = dict()
tnum = 0
font = ImageFont.truetype("C:/Windows/Fonts/msgothic.ttc", 24)
img = Image.new("RGB", (300, 50), (0,0, 0))
draw = ImageDraw.Draw(img)



root = Tk()
root.title("Target_Typing")
root.geometry(DisplayPos())
root.resizable(False, False)
# root.protocol("WM_DELETE_WINDOW", False)


style = ttk.Style()
style.configure("light.TFrame", background="#2f4f4f")
style.configure("light.TButton", font=("Yu Gothic UI", 12))
style.configure("light.TRadiobutton", font=("Yu Gothic UI", 12))

quitB = ttk.Button(root, text="Quit", style="light.TButton", padding=[15, 10], command=Quit)
titlestartB = ttk.Button(root, text="Start", style="light.TButton", padding=[15, 10], command=PreGame)
titleL = ttk.Label(root, text="Target Typing!", relief="ridge", font=("Times New Roman", 40), padding=[15], foreground="#19448e", background="#e0f0ff")

optionL1 = ttk.Label(root, text="Game Settings", font=("Times New Roman", 30), padding=[10], foreground="#191970")
optionL2 = ttk.Label(root, text="Types of vocabulary books", font=("Arial", 20))
optionL3 = ttk.Label(root, text="Amount of questions", font=("Arial", 20))
optionL4 = ttk.Label(root, text="Enter any number", font=("Yu Gothic UI", 12))
optionL5 = ttk.Label(root, text="Test range", font=("Arial", 20))
optionL6 = ttk.Label(root, text="Enter any number", font=("Yu Gothic UI", 12))
optionF1 = ttk.Frame(root, width=540, height=4, style="light.TFrame")
booktype = tk.IntVar(root, value=0)
booktypeRB0 = ttk.Radiobutton(root, text="Target-1400 (test)", style="light.TRadiobutton", value=0, variable=booktype, command=NumCheck)
booktypeRB1 = ttk.Radiobutton(root, text="Target-1900", style="light.TRadiobutton", value=1, variable=booktype, state="", command=NumCheck)
tcl_Validate = root.register(isOk)
amountE = ttk.Entry(root, justify="right", validate="key", validatecommand=(tcl_Validate, "%P","%S"))
startB = ttk.Button(root, text="Start!", style="light.TButton", padding=[10, 5], command=StartScreen)
returnB = ttk.Button(root, text="Return", style="light.TButton", padding=[10, 5], command=TitleScreen)

countdown = tk.StringVar(root)
countdownL = ttk.Label(root, textvariable=countdown, font=("Arial", 120))


watch = tk.StringVar(root, value="0.00 sec")
word_fg = tk.StringVar(root)
word_bg = tk.StringVar(root)
meaning = tk.StringVar(root)
qamtI = tk.IntVar(root)
qamtS = tk.StringVar(root)
watchL = ttk.Label(root, textvariable=watch, font=("Arial", 20), padding=[5, 5])
meaningL = ttk.Label(root, textvariable=meaning, font=("Arial", 20), padding=[5, 5])
exitB = ttk.Button(root, text="exit", style="light.TButton", padding=[10, 5], command=ForcedReturn)
wordC1 = tk.Canvas(root, width=640, height=50, bg="#f0f0f0")
bg_text = wordC1.create_text(0, 0, text="")
fg_text = wordC1.create_text(0, 0, text="")
circleL = ttk.Label(root, text="〇", font=("Yu Gothic UI", 200,"bold"), foreground="#ff0000")
qamtL = ttk.Label(root, textvariable=qamtS, font=("Arial", 20), padding=[5, 5])


if startflag == False:
    TitleScreen()
    startflag = True


root.mainloop()
