from tkinter import *
import random
tk =Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
for m in range(0,101):
    g = ['red', 'pink', 'green','gray']
    h = random.randint(0,2)
    a = random.randint(0, 400)
    b = random.randint(0, 400)
    c = random.randint(0, 400)
    d = random.randint(0, 400)
    e = random.randint(0, 400)
    f = random.randint(0, 400)
    canvas.create_polygon(a, b, c, d, e, f, fill=g[h],outline="black")
    g = ['red', 'pick', 'green']
tk.mainloop()