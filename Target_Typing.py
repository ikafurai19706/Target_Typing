# coding: utf-8
import multiprocessing as m_process
import hashlib
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

checksum = open('1400-test.txt', 'rb')
if hashlib.sha256(checksum.read()).hexdigest() == '83361224e1eaa0c43535d381d248ce04e7b4b9b5b469cdd1a0e0884c8508e234':
    checksum.close()
else:
    checksum.close()
    messagebox.showerror('integrity error', 'File data is corrupted.')
    exit()

def SetDisplayPos():
    S_width = root.winfo_screenwidth()
    S_height = root.winfo_screenheight()
    W_width = S_width//2 - 320
    W_height = S_height//2 - 240
    return '640x480+'+str(W_width)+'+'+str(W_height)

def PlaceTitleScreen():
    b1.pack(side='bottom', pady=30)
    b2.pack(side='bottom')
    l1.pack(pady=100)
    
def  ResetScreen():
    b1.forget()
    b2.forget()
    l1.forget()
    rb1_1.forget()
    rb1_2.forget()

def PreGame():
    ResetScreen()
    l2.place(x=320, y=50, anchor='center')
    rb1_1.place(x=240, y=150, anchor='center')
    rb1_2.place(x=400, y=150, anchor='center')

StartFlag = False
root = Tk()
root.title('Target_Typing')
root.geometry(SetDisplayPos())
root.resizable(False, False)
root.protocol('WM_DELETE_WINDOW', False)

b1 = ttk.Button(root, text='QUIT', padding=[15,10], command=exit)
b2 = ttk.Button(root, text='START', padding=[15,10], command=PreGame)
l1 = ttk.Label(root, text='Target Typing!', relief='ridge', font=('Arial', 40), padding=[10])

l2 = ttk.Label(root, text='Game Settings', font=('Arial', 30), padding=[15])
rvar1 = tk.IntVar(value=2)
rb1_1 = ttk.Radiobutton(root, text='rb1', value=1, variable=rvar1)
rb1_2 = ttk.Radiobutton(root, text='rb2', value=2, variable=rvar1)

if StartFlag == False:
    PlaceTitleScreen()
    StartFlag = True


root.mainloop()
