from tkinter import *
from time import *

def update():
    time_string=strftime("%I:%M:%S %p")#%I--> for hour   %M--> for minutes  %S-->for seconds
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d,%Y")
    date_label.config(text=date_string)

    windows.after(1000,update)#to show the mov't pf seconds

windows=Tk()


time_label=Label(windows,font=("Arial",50),fg="green",bg="black")
time_label.pack()

day_label=Label(windows,font=("Ink Free",25))
day_label.pack()

date_label=Label(windows,font=("Ink Free",30))
date_label.pack()


update()
windows.mainloop()
