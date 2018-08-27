
from tkinter import *
tk =Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
canvas.create_polygon(10,10,100,10,100,110,fill="",
outline="black")
import random
a = random.randint(0,255)
b = random.randint(0,255)
c = random.randint(0,255)
canvas.color(a,b,c)

tk.mainloop()