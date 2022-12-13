# coding: utf-8
import threading as th
import tkinter as tk
import time, re, random, sys, keyboard, textwrap, pyautogui
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageFont, ImageDraw
from simpleaudio import WaveObject


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
	optionL5.pack_forget()
	optionL6.place_forget()
	countdownL.pack_forget()
	meaningL.place_forget()
	circleL.place_forget()
	qamtL.place_forget()
	booktypeRB0.place_forget()
	booktypeRB1.place_forget()
	amountE.place_forget()
	rangefE.place_forget()
	rangelE.place_forget()
	optionF1.pack_forget()
	watchL.pack_forget()
	

def TitleScreen():
	global pregame
	pregame = False
	ResetScreen()
	quitB.pack(side="bottom", pady=30)
	titlestartB.pack(side="bottom")
	titleL.pack(pady=100)

	
def PreGame():
	global pregame
	pregame = True
	ResetScreen()
	optionL1.pack(pady=3)
	optionF1.pack(pady=5)
	optionL2.pack(pady=5)
	booktypeRB0.place(x=200, y=150, anchor="center")
	booktypeRB1.place(x=440, y=150, anchor="center")
	optionL3.pack(pady=40)
	optionL4.place(x=250, y=230,anchor="center")
	amountE.place(x=390, y=230, anchor="center")
	if amountE.get() == "":
		amountE.insert(index="end", string="10")
	optionL5.pack()
	optionL6.place(x=320, y=310, anchor="center")
	rangefE.place(x=240, y=310, anchor="center")
	if rangefE.get() == "":
		rangefE.insert(index="end", string="1")
	rangelE.place(x=400, y=310, anchor="center")
	if rangelE.get() == "":
		rangelE.insert(index="end", string="10")
	startB.pack(side="right", anchor="se", padx=5, pady=5)
	returnB.pack(side="right", anchor="se", padx=5, pady=5)

def BlankCheck():
	try:
		check = bool(int(amountE.get()) == 0 or int(rangefE.get()) == 0 or int(rangelE.get()) == 0 or int(amountE.get()) > abs(int(rangefE.get()) - int(rangelE.get())) + 1)
	except ValueError:
		check = True
	return check

def NumCheck():
	if BlankCheck():
		return
	if int(amountE.get()) > 200 and booktype.get() == 0:
		amountE.delete(first=0, last="end")
		amountE.insert(index="end", string="200")
	elif int(amountE.get()) > 1900 and booktype.get() == 1:
		amountE.delete(first=0, last="end")
		amountE.insert(index="end", string="1900")
	if int(rangefE.get()) > 200 and booktype.get() == 0:
		rangefE.delete(first=0, last="end")
		rangefE.insert(index="end", string="200")
	elif int(rangefE.get()) > 1900 and booktype.get() == 1:
		rangefE.delete(first=0, last="end")
		rangefE.insert(index="end", string="1900")
	if int(rangelE.get()) > 200 and booktype.get() == 0:
		rangelE.delete(first=0, last="end")
		rangelE.insert(index="end", string="200")
	elif int(rangelE.get()) > 1900 and booktype.get() == 1:
		rangelE.delete(first=0, last="end")
		rangelE.insert(index="end", string="1900")

def isOk(num, diff):
	if num == "":
		return True
	if not re.match(re.compile("[0-9]+"), diff):
		root.bell()
		return False
	if int(num) > 200 and booktype.get() == 0:
		amountE.delete(first=0, last="end")
		amountE.insert(index="end", string="200")
		return False
	elif int(num) > 1900 and booktype.get() == 1:
		amountE.delete(first=0, last="end")
		amountE.insert(index="end", string="1900")
		return False
	return True

def isOk_rf(num, diff):
	if num == "":
		return True
	if not re.match(re.compile("[0-9]+"), diff):
		root.bell()
		return False
	if int(num) > 200 and booktype.get() == 0:
		rangefE.delete(first=0, last="end")
		rangefE.insert(index="end", string="200")
		return False
	elif int(num) > 1900 and booktype.get() == 1:
		rangefE.delete(first=0, last="end")
		rangefE.insert(index="end", string="1900")
		return False
	return True

def isOk_rl(num, diff):
	if num == "":
		return True
	if not re.match(re.compile("[0-9]+"), diff):
		root.bell()
		return False
	if int(num) > 200 and booktype.get() == 0:
		rangelE.delete(first=0, last="end")
		rangelE.insert(index="end", string="200")
		return False
	elif int(num) > 1900 and booktype.get() == 1:
		rangelE.delete(first=0, last="end")
		rangelE.insert(index="end", string="1900")
		return False
	return True



def StartScreen():
	global pregame
	if pregame:
		pregame = False
	else:
		return
	if BlankCheck():
		messagebox.showerror("Error", "Invalid value entered.")
		return
	global lines, w_len, originlines, tnum
	if booktype.get() == 0:
		with open("1400-test.txt", "r", encoding="utf-8") as f:
			originlines = f.readlines()
	elif booktype.get() == 1:
		with open("1900.txt", "r", encoding="utf-8") as f:
			originlines = f.readlines()
	lines = list(map(lambda s:s.rstrip("\n"), originlines))
	print(lines)
	w_len = int(amountE.get())
	t[tnum] = th.Thread(target=StartFunc1)
	t[tnum].setDaemon(True)
	t[tnum].start()
	tnum += 1

def StartFunc1():
	global running, tnum, found, stop
	if running:
		return
	running = True
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
	global stop, bg_text, fg_text, typing
	typing = True
	qamtI.set(1)
	qamtL.place(x=0, y=240, anchor="w")
	wordC1.place(x=320,y=180, anchor="center")
	if int(rangefE.get()) <= int(rangelE.get()):
		rf, rl = int(rangefE.get()), int(rangelE.get())
	else:
		rf, rl = int(rangelE.get()), int(rangefE.get())
	for i in random.sample(lines[rf-1:rl], w_len):
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
				sound_type.play()
			elif search != "":
				sound_miss.play()
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
	global stop, found, typing
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
	global stop, pregame
	stop = True
	TitleScreen()

def Quit():
	sys.exit()


running = False
pregame = False
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
optionL5 = ttk.Label(root, text="Exam coverage", font=("Arial", 20))
optionL6 = ttk.Label(root, text="～", font=("Yu Gothic UI", 15))
optionL7 = ttk.Label(root, text="Others", font=("Arial", 20))
optionF1 = ttk.Frame(root, width=540, height=4, style="light.TFrame")
booktype = tk.IntVar(root, value=0)
booktypeRB0 = ttk.Radiobutton(root, text="Target-1400 (test)", style="light.TRadiobutton", value=0, variable=booktype, command=NumCheck)
booktypeRB1 = ttk.Radiobutton(root, text="Target-1900", style="light.TRadiobutton", value=1, variable=booktype, state="", command=NumCheck)
tcl_Validate = root.register(isOk)
tcl_Validate_rf = root.register(isOk_rf)
tcl_Validate_rl = root.register(isOk_rl)
amountE = ttk.Entry(root, width=10, justify="right", validate="key", validatecommand=(tcl_Validate, "%P","%S"))
rangefE = ttk.Entry(root, width=10, justify="right", validate="key", validatecommand=(tcl_Validate_rf, "%P","%S"))
rangelE = ttk.Entry(root, width=10, justify="right", validate="key", validatecommand=(tcl_Validate_rl, "%P","%S"))
startB = ttk.Button(root, text="Start!", style="light.TButton", padding=[10, 5], command=StartScreen)
returnB = ttk.Button(root, text="Return", style="light.TButton", padding=[10, 5], command=TitleScreen)

countdown = tk.StringVar(root)
countdownL = ttk.Label(root, textvariable=countdown, font=("Arial", 120))

sound_type = WaveObject.from_wave_file("sounds/type.wav")
sound_miss = WaveObject.from_wave_file("sounds/miss.wav")
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
