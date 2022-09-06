﻿# coding: utf-8
import multiprocessing as m_process
from tkinter import *
from tkinter import ttk

def SetDisplayPos():
    S_width = root.winfo_screenwidth()
    S_height = root.winfo_screenheight()
    W_width = S_width//2 - 320
    W_height = S_height//2 - 240
    return '640x480+'+str(W_width)+'+'+str(W_height)

def PlaceTitleScreen():
    button1.pack(side='bottom', pady=30)
    button2.pack(side='bottom')
    label1.pack(pady=100)
    
def ForgetAllWidget():
    button1.forget()
    button2.forget()
    label1.forget()

StartFlag = False
root = Tk()
root.title('Target_Typing')
root.geometry(SetDisplayPos())
root.resizable(False, False)
root.protocol('WM_DELETE_WINDOW', False)

button1 = ttk.Button(root, text='QUIT', padding=[15,10], command=exit)
button2 = ttk.Button(root, text='START', padding=[15,10], command=ForgetAllWidget)
label1 = ttk.Label(root, text='Target Typing!', relief='ridge', font=("Arial", 40), padding=[10])

if StartFlag == False:
    PlaceTitleScreen()
    StartFlag = True


root.mainloop()