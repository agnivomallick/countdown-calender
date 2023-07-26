from tkinter import *
from datetime import *

def get_events():
    list_events=[]
    with open("events.txt") as file:
        for line in file:
            line=line.rstrip("\n")
            current_event=line.split(",")
            event_date=datetime.strptime(current_event[1], "%d/%m/%y").date()
            current_event[1]=event_date
            list_events.append(current_event)
    return list_events

def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split(" ")
    return number_of_days[0]


root=Tk()
root.geometry("700x620")
root.title("Countdown Calender")
root.iconbitmap("calender.ico")
c=Canvas(root, width=900, height=800, bg="black")
c.pack()
c.create_text(100, 50, anchor="w", fill="orange", font="Arial 28 bold underline", text="Important Dates")

events = get_events()
today = date.today()

vertical_space = 100

for event in events:
    event_name = event[0]
    days_until = days_between_dates(event[1], today)
    display = "It is %s days until %s" %(days_until, event_name)
    if (int(days_until) <= 7):
        text_col = "red"
    else:
        text_col = "lightblue"
    
    
    c.create_text(100, vertical_space, anchor='w', fill=text_col, font="Arial 28", text=display)

    vertical_space = vertical_space + 30


root.mainloop()