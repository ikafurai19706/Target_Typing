# coding: utf-8
import multiprocessing as m_process
import sys, hashlib
from tkinter import *
from tkinter import ttk

checksum = open('1400-test.txt', 'rb')
if hashlib.sha256(checksum.read()).hexdigest == '805124a934de883955882e3986311bbf78db34c63c8c9ba62f329079a76a9d08':
    checksum.close()
else:
    checksum.close()
    sys.exit()

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
    
def  ResetScreen():
    button1.forget()
    button2.forget()
    label1.forget()

StartFlag = False
root = Tk()
root.title('Target_Typing')
root.geometry(SetDisplayPos())
root.resizable(False, False)
root.protocol('WM_DELETE_WINDOW', False)

button1 = ttk.Button(root, text='QUIT', padding=[15,10], command=sys.exit)
button2 = ttk.Button(root, text='START', padding=[15,10], command=ResetScreen)
label1 = ttk.Label(root, text='Target Typing!', relief='ridge', font=("Arial", 40), padding=[10])

if StartFlag == False:
    PlaceTitleScreen()
    StartFlag = True


root.mainloop()
