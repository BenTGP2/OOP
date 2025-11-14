import tkinter as tk
from tkinter import *

QueueUI = Tk()
QueueUI.geometry("1920x1080")

Queue_Text_Box = tk.Text(width=50, height=20)
Queue_Text_Box.place(x=100, y=100)

Stack_Text_Box = tk.Text(width=50, height=20)
Stack_Text_Box.place(x=100, y=450)

QueueTitle = tk.Label(text="Elements in Queue:")
QueueTitle.place(x=100, y=80)

QueueEnterTitle = tk.Label(text="Element to add to Queue:")
QueueEnterTitle.place(x=550, y=80)

StackEnterTitle = tk.Label(text="Element to push to Stack:")
StackEnterTitle.place(x=550, y=430)

StackTitle = tk.Label(text="Elements in Stack:")
StackTitle.place(x=100, y=430)

QueueEnterUI = Text(width=55, height=2)
QueueEnterUI.place(x=550, y=100)

StackEnterUI = Text(width=55, height=2)
StackEnterUI.place(x=550, y=450)

class Queue:
    def __init__(self):
        self.queue = []

class Stack:
    def __init__(self):
        self.stack = []

def show(x):
    try:
        if x == "QueueEnter":
            QueueElement = QueueEnterUI.get("1.0","end-1c")
            Queue_Text_Box.insert(END, QueueElement + "\n")
        elif x == "StackEnter":
            StackElement = StackEnterUI.get("1.0","end-1c")
            Stack_Text_Box.insert(END, StackElement + "\n")
        elif x == "Dequeue":
            Queue_Text_Box.delete(1.0, END)
        elif x == "Pop":
            Stack_Text_Box.delete(1.0, END)
        elif x == "ConvertToStack":
            QueueElements = Queue_Text_Box.get("1.0", "end-1c")
            Stack_Text_Box.insert(END, QueueElements)
        elif x == "ConvertToQueue":
            StackElements = Stack_Text_Box.get("1.0", "end-1c")
            Queue_Text_Box.insert(END, StackElements)
        else:
            print("Something went wrong I dunno")
    except:
        print("Something went wrong I dunno")
#Main

q1 = Queue()
s1 = Stack()

B1 = Button(QueueUI, text="Queue", width=10, height=5, command=lambda: show("QueueEnter"))
B1.place(x=1000, y=65)
B2 = Button(QueueUI, text="Dequeue", width=10, height=5, command=lambda: show("Dequeue"))
B2.place(x=1100, y=65)
B3 = Button(QueueUI, text="To Stack", width=10, height=5, command=lambda: show("ConvertToStack"))
B3.place(x=1200, y=65)
B4 = Button(QueueUI, text="Push", width=10, height=5, command=lambda: show("StackEnter"))
B4.place(x=1000, y=430)
B5 = Button(QueueUI, text="Pop", width=10, height=5, command=lambda: show("Pop"))
B5.place(x=1100, y=430)
B6 = Button(QueueUI, text="To Queue", width=10, height=5, command=lambda: show("ConvertToQueue"))
B6.place(x=1200, y=430)

QueueUI.mainloop()
Queue_Text_Box.mainloop()
Stack_Text_Box.mainloop()
