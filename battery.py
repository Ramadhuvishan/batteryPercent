import psutil
import time
from tkinter import *

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
if(plugged):
    plugged = "YES"
else:
    plugged = "NO"

master = Tk()
menu = Menu(master)
master.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Info')
filemenu.add_separator()
filemenu.add_command(label='Exit',command=master.quit)

messageVar = Message(master, text ='Battery Percentage: '+percent+'% \nCharger Plugged:    '+plugged )
if(percent>='80'):
    messageVar.config(bg='lightgreen')
elif(percent>='50' and percent<='79'):
    messageVar.config(bg='orange')
else:
    messageVar.config(bg='red')
messageVar.pack()
master.geometry("500x200")
mainloop()
