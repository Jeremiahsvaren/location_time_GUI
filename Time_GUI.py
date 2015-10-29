from datetime import datetime
from pytz import timezone
from Tkinter import *
import ttk

fmt = "%H%M"
gui_fmt = "%I:%M %p"

# Current time in London
now_london = datetime.now(timezone('UTC'))
london_time = int(now_london.strftime(fmt))
london_gui_time = now_london.strftime(gui_fmt)

# Convert to US/Pacific time zone
now_portland = now_london.astimezone(timezone('US/Pacific'))
portland_time = int(now_portland.strftime(fmt))
portland_gui_time = now_portland.strftime(gui_fmt)

# Convert to New York time zone
now_new_york = now_portland.astimezone(timezone('US/Eastern'))
new_york_time = int(now_new_york.strftime(fmt))
new_york_gui_time = now_new_york.strftime(gui_fmt)

#Check New Yorks Office
if new_york_time >= 900 and new_york_time <= 2100:
    NY_branch = "OPEN"
else:
    NY_branch = "CLOSED"

#Check Londons Office
if london_time >= 900 and london_time <= 2100:
    london_branch = "OPEN"
else:
    london_branch = "CLOSED"

#Check Portlands Office
if portland_time >= 900 and portland_time <= 2100:
    portland_branch = "OPEN"
else:
    portland_branch = "CLOSED"


root = Tk()
root.title("Branch Hours")
mainframe = ttk.Frame(root, height=600, width=800)
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))

Label(mainframe, text="Location").grid(column=0, row=0)
Label(mainframe, text="Local Time").grid(column=1, row=0)
Label(mainframe, text="Open/Closed").grid(column=2, row=0)

#Portlands info
Label(mainframe, text="Portland HQ").grid(column=0, row=1)
Label(mainframe, text=portland_gui_time).grid(column=1, row=1)
Label(mainframe, text=portland_branch).grid(column=2, row=1)

#New Yorks Info
Label(mainframe, text="New York Branch").grid(column=0, row=2)
Label(mainframe, text=new_york_gui_time).grid(column=1, row=2)
Label(mainframe, text=NY_branch).grid(column=2, row=2)

#Londons Info
Label(mainframe, text="London Branch").grid(column=0, row=3)
Label(mainframe, text=london_gui_time).grid(column=1, row=3)
Label(mainframe, text=london_branch).grid(column=2, row=3)


root.mainloop()
