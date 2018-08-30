from tkinter import *
import random
tk =Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
for m in range(0,3):
    g = ['red', 'pink', 'green','gray']
    h = random.randint(0,2)
    a = 10
    b = 10
    c = 100
    d = 10
    e = 100
    f = 110
    canvas.create_polygon(a,b,c,d,e,f,fill=g[h],outline="black")
    x = ['red', 'pink', 'green', 'gray']
    u = random.randint(0,3)
    i = a + 90
    j = b
    k = c * 2
    l = d
    m = e * 2
    n = f
    canvas.create_polygon(i,j,k,l,m,n,fill=x[u],outline="black")
    y = ['red', 'pink', 'green', 'gray']
    z = random.randint(0, 2)
    o = i + 90
    p = j
    q = k + 100
    r = l
    s = m + 100
    t = n
    canvas.create_polygon(o,p,q,r,s,t,fill=y[z],outline="black")
tk.mainloop()


