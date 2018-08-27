# def hello():
#     print('hello there')
# from tkinter import *
# tk = Tk()
# btn = Button(tk,text="click me",command=hello)
# btn.pack()
# tk.mainloop()
from tkinter import *

import random
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
def random_rectangle(width,height,fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1,y1,x2,y2,fill=fill_color)

for x in range(0,100):
    random_rectangle(400,400,'#ffd800')
tk.mainloop()