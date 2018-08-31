from tkinter import *
import random

tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()


def box():
    triangle_num = input()
    triangle_num = int(triangle_num)

    t = ['red', 'green', 'orange', 'yellow', 'blue', 'pink']

    a_x = 10
    a_y = 10

    b_x = 100
    b_y = 10

    c_x = 100

    c_y = 110

    move = b_x - a_x

    count = 0
    while count <= triangle_num:
        jj = random.randint(0, 3)
        canvas.create_polygon(a_x, a_y, b_x, b_y, c_x, c_y, fill=t[jj], outline="black")
        a_x = a_x + move
        b_x = b_x + move
        c_x = c_x + move
        count = count + 1


box()
tk.mainloop()
