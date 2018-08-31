'''
输入几排几列，画出三角形矩阵
'''
from tkinter import *
import random

'''
画一排三角形，每一排三角形有number个
'''


def draw_triangle_row(number, a_y, b_y, c_y):
    triangle_num = int(number)
    t = ['red', 'green', 'orange', 'yellow', 'blue', 'pink']

    a_x = 10
    b_x = 100
    c_x = 100

    move_x = b_x - a_x
    count = 1
    while count <= triangle_num:
        jj = random.randint(0, 5)
        canvas.create_polygon(a_x, a_y, b_x, b_y, c_x, c_y, fill=t[jj], outline="black")
        a_x = a_x + move_x
        b_x = b_x + move_x
        c_x = c_x + move_x
        count = count + 1


tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()

num = input()
ber = input()
row_num = int(ber)

aa_y = 10
bb_y = 10
cc_y = 110

move_y = cc_y - bb_y
'''
画row_num排三角形
'''
count_line = 1
while count_line <= row_num:
    draw_triangle_row(num, aa_y, bb_y, cc_y)
    aa_y = aa_y + move_y
    bb_y = bb_y + move_y
    cc_y = cc_y + move_y
    count_line = count_line + 1

tk.mainloop()
