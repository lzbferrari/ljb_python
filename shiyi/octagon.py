'''
用创造一个红色的八边形
'''
import turtle
t = turtle.Pen()
t.color(1, 0, 0)
t.begin_fill()

for x in range(1,9):

    t.forward(100)
    t.right(45)#这里

t.end_fill()


