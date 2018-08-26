'''
创造一个可以点的按钮，点一次就会打印一个hello
'''
import tkinter
tkinter._test()
from tkinter import *

def hello():
    print('hello')
tk = Tk()
btn = Button(tk,text="click me",command=hello)
btn.pack()

tk.mainloop()


