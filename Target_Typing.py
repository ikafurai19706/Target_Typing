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

def  ResetScreen():
    b1.pack_forget()
    b2.pack_forget()
    b3.pack_forget()
    b4.pack_forget()
    l1.pack_forget()
    l2.pack_forget()
    l3.place_forget()
    rb1_1.place_forget()
    rb1_2.place_forget()
    

def PlaceTitleScreen():
    ResetScreen()
    b1.pack(side='bottom', pady=30)
    b2.pack(side='bottom')
    l1.pack(pady=100)

def PreGame():
    ResetScreen()
    l2.pack(pady=10)
    l3.place(x=320, y=110, anchor='center')
    rb1_1.place(x=200, y=150, anchor='center')
    rb1_2.place(x=440, y=150, anchor='center')
    b3.pack(side='right', anchor='se', padx=5, pady=5)
    b4.pack(side='right', anchor='se', padx=5, pady=5)


StartFlag = False
root = Tk()
root.title('Target_Typing')
root.geometry(SetDisplayPos())
root.resizable(False, False)
# root.protocol('WM_DELETE_WINDOW', False)

style = ttk.Style()
style.configure('light.TButton', font=('Yu Gothic UI', 12))
style.configure('light.TRadiobutton', font=('Yu Gothic UI', 12))

b1 = ttk.Button(root, text='Quit', style='light.TButton', padding=[15, 10], command=exit)
b2 = ttk.Button(root, text='Start', style='light.TButton', padding=[15, 10], command=PreGame)
l1 = ttk.Label(root, text='Target Typing!', relief='ridge', font=('Arial', 40), padding=[15])

l2 = ttk.Label(root, text='Game Settings', relief='ridge', font=('Arial', 30), padding=[10])
l3 = ttk.Label(root,text='     Types of vocabulary books     ', font=('Arial', 20, 'underline'))
rvar1 = tk.IntVar(value=2)
rvar1.set(0)
rb1_1 = ttk.Radiobutton(root, text='Target 1400(test)', style='light.TRadiobutton', value=0, variable=rvar1)
rb1_2 = ttk.Radiobutton(root, text='Target 1900(unavailable)', style='light.TRadiobutton', value=1, variable=rvar1, state='disabled')
b3 = ttk.Button(root, text='Start!', style='light.TButton', padding=[10, 5], command='')
b4 = ttk.Button(root, text='Return', style='light.TButton', padding=[10, 5], command=PlaceTitleScreen)

if StartFlag == False:
    PlaceTitleScreen()
    StartFlag = True


root.mainloop()
