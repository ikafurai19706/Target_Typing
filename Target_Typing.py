# coding: utf-8
import threading as th
import hashlib, time, re, random, sys, keyboard
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageFont, ImageDraw
import pyautogui


with open("1400-test.txt", "rb") as checksum:
    if hashlib.md5(checksum.read()).hexdigest() != "4c8e5ddbcda1bf1072945106ceaa2a19":
        messagebox.showerror("Integrity error", "File data is corrupted.")
        sys.exit()


def DisplayPos():
    S_width = root.winfo_screenwidth()
    S_height = root.winfo_screenheight()
    W_width = S_width//2 - 320
    W_height = S_height//2 - 240
    return "640x480+"+str(W_width)+"+"+str(W_height)


def  ResetScreen():
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    b5.pack_forget()
    c1.delete(bg_text)
    c1.delete(fg_text)
    c1.place_forget()
    l1.pack_forget()
    l2.pack_forget()
    l3.pack_forget()
    l4.pack_forget()
    l5.place_forget()
    l6.pack_forget()
    l8.place_forget()
    l9.place_forget()
    l10.place_forget()
    rb1_1.place_forget()
    rb1_2.place_forget()
    e1.place_forget()
    f1.pack_forget()
    watch.pack_forget()
    

def TitleScreen():
    ResetScreen()
    b1.pack(side="bottom", pady=30)
    b2.pack(side="bottom")
    l1.pack(pady=100)

    
def PreGame():
    ResetScreen()
    l2.pack(pady=10)
    f1.pack(pady=5)
    l3.pack(pady=5)
    rb1_1.place(x=200, y=160, anchor="center")
    rb1_2.place(x=440, y=160, anchor="center")
    l4.pack(pady=40)
    l5.place(x=250, y=240,anchor="center")
    e1.place(x=390, y=240, anchor="center")
    e1.insert(index=tk.END, string="10")
    b3.pack(side="right", anchor="se", padx=5, pady=5)
    b4.pack(side="right", anchor="se", padx=5, pady=5)

def NumCheck():
    if int(e1.get()) > 200 and rvar1.get() == 0:
        e1.delete(first=0,last=tk.END)
        e1.insert(index=tk.END, string="200")
        return False
    elif int(e1.get()) > 1900 and rvar1.get() == 1:
        e1.delete(first=0,last=tk.END)
        e1.insert(index=tk.END, string="1900")
        return False

def isOk(num, diff):
    if num == "":
        e1.delete(first=0,last=tk.END)
        e1.insert(index=tk.END, string="1")
        return False
    if not re.match(re.compile("[0-9]+"), diff):
        root.bell()
        return False
    if int(num) > 200 and rvar1.get() == 0:
        e1.delete(first=0,last=tk.END)
        e1.insert(index=tk.END, string="200")
        return False
    elif int(num) > 1900 and rvar1.get() == 1:
        e1.delete(first=0,last=tk.END)
        e1.insert(index=tk.END, string="1900")
        return False
    return True



def StartScreen():
    if int(e1.get()) == 0:
        root.bell()
        return
    global lines
    global w_len
    global originlines
    global tnum
    if rvar1.get() == 0:
        with open("1400-test.txt", "r", encoding="utf-8") as f:
            originlines = f.readlines()
    elif rvar1.get() == 1:
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
    l6.place(x=320, y=240, anchor="center")
    for i in reversed(range(1, 4)):
        lvar1.set(i)
        time.sleep(1)
    l6.place_forget()
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
    lvar5.set(1)
    l10.place(x=0, y=240, anchor="w")
    c1.place(x=320,y=180, anchor="center")
    for i in random.sample(lines, w_len):
        fg_text = c1.create_text(0, 0, text="")
        lvar3.set("")
        j = 0
        word_r = i.split(",")
        word_r_len = len(word_r[0])
        lvar3_b.set(word_r[0])
        w, h = draw.textsize(word_r[0], font)
        print(w, h)
        bg_text = c1.create_text(320, 25, text=lvar3_b.get(), anchor="center", font=("MS Gothic", 20), fill="gray")
        fg_w = 320 - (w/1.7)
        lvar4.set(word_r[1])
        while j < word_r_len:
            t = str(keyboard.read_event())
            if stop:break
            try:
                search = re.search(pattern, t, flags=re.IGNORECASE).group()
            except AttributeError:          
                search = ""
            print(search)
            if search == word_r[0][j]:
                lvar3.set(str(lvar3.get())+word_r[0][j])
                j += 1
                c1.delete(fg_text)
                fg_text = c1.create_text(fg_w, 25, text=lvar3.get(), anchor="w", font=("MS Gothic", 20))
        if stop:break
        l9.place(x=320, y=240, anchor="center")
        typing = False
        time.sleep(0.8)
        if lvar5.get() == int(e1.get()):
            ForcedReturn()
            break
        l9.place_forget()
        c1.delete(bg_text)
        c1.delete(fg_text)
        lvar5.set(lvar5.get()+1)
        typing = True
        


def MainGame2():
    global stop
    global found
    global typing
    tempTime = 0
    b5.pack(side="bottom", anchor="se")
    l8.place(x=320, y=240, anchor="center")
    watch.pack(anchor='nw')
    while not stop:
        while not typing:
            if stop:break
            time.sleep(0.1)
        startTime = time.time()
        while typing:
            if stop:break
            currentTime = time.time()
            dispTime = round(currentTime - startTime + tempTime, 2)
            if dispTime >= 100:
                lvar2.set(str(dispTime).ljust(6,"0")+" sec")
            elif dispTime >= 10:
                lvar2.set(str(dispTime).ljust(5,"0")+" sec")
            else:
                lvar2.set(str(dispTime).ljust(4,"0")+" sec")
        tempTime = dispTime
    watch.pack_forget()


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

b1 = ttk.Button(root, text="Quit", style="light.TButton", padding=[15, 10], command=Quit)
b2 = ttk.Button(root, text="Start", style="light.TButton", padding=[15, 10], command=PreGame)
l1 = ttk.Label(root, text="Target Typing!", relief="ridge", font=("Times New Roman", 40), padding=[15], foreground="#4169e1", background="#f0f8ff")

l2 = ttk.Label(root, text="Game Settings", font=("Times New Roman", 30), padding=[10], foreground="#191970")
l3 = ttk.Label(root, text="Types of vocabulary books", font=("Arial", 20))
l4 = ttk.Label(root, text="Number of questions", font=("Arial", 20))
l5 = ttk.Label(root, text="Enter any number", font=("Yu Gothic UI", 12))
f1 = ttk.Frame(root, width=540, height=4, style="light.TFrame")
rvar1 = tk.IntVar(root, value=0)
rb1_1 = ttk.Radiobutton(root, text="Target-1400 (test)", style="light.TRadiobutton", value=0, variable=rvar1, command=NumCheck)
rb1_2 = ttk.Radiobutton(root, text="Target-1900 (unavailable)", style="light.TRadiobutton", value=1, variable=rvar1, state="", command=NumCheck)
tcl_Validate = root.register(isOk)
e1 = ttk.Entry(root, justify="right", validate="key", validatecommand=(tcl_Validate, "%P","%S"))
b3 = ttk.Button(root, text="Start!", style="light.TButton", padding=[10, 5], command=StartScreen)
b4 = ttk.Button(root, text="Return", style="light.TButton", padding=[10, 5], command=TitleScreen)

lvar1 = tk.StringVar(root)
l6 = ttk.Label(root, textvariable=lvar1, font=("Arial", 120))


lvar2 = tk.StringVar(root, value="0.000 sec")
lvar3 = tk.StringVar(root)
lvar3_b = tk.StringVar(root)
lvar4 = tk.StringVar(root)
lvar5 = tk.IntVar(root, value=0)
watch = ttk.Label(root, textvariable=lvar2, font=("Arial", 20), padding=[5, 5])
l8 = ttk.Label(root, textvariable=lvar4, font=("Arial", 20), padding=[5, 5])
b5 = ttk.Button(root, text="exit", style="light.TButton", padding=[10, 5], command=ForcedReturn)
c1 = tk.Canvas(root, width=640, height=50, bg="#f0f0f0")
bg_text = c1.create_text(0, 0, text="")
fg_text = c1.create_text(0, 0, text="")
l9 = ttk.Label(root, text="〇", font=("Yu Gothic UI", 200,"bold"), foreground="#ff0000")
l10 = ttk.Label(root, textvariable=lvar5, font=("Arial", 20), padding=[5, 5])


if startflag == False:
    TitleScreen()
    startflag = True


root.mainloop()