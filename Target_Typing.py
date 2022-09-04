# coding: utf-8
import multiprocessing as mprocess
from tkinter import *
from tkinter import ttk

def SetDisplayPos():
    Swidth = root.winfo_screenwidth()
    Sheight = root.winfo_screenheight()
    Wwidth = Swidth//2 - 320
    Wheight = Sheight//2 - 240
    return '640x480+'+str(Wwidth)+'+'+str(Wheight)

root = Tk()
root.title('Target_Typing')
root.geometry(SetDisplayPos())
root.resizable(False, False)

button = ttk.Button(root,text='button')
label1 = ttk.Label(root,text='label')

button.pack(side='bottom')
label1.pack()

root.mainloop()