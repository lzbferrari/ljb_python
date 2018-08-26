'''
创造一个可以输入边长大小和要几个角的海龟画图，python可以自动画出你要的星星
'''
import turtle

t = turtle.Pen()
t.color(1,0,0)
t.begin_fill()
def draw_star(size, points):
    aa = 180 / points
    bb = 540 / points
    i = 0
    num = points * 2
    while i < num:
        t.forward(size)
        if i % 2 == 0:
            t.left(180 - bb)
        else:
            t.right(180 - aa)
        i = i + 1
a = input()
b = int(a)
c = input()
d = int(c)
draw_star(b,d)
t.end_fill()