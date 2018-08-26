'''
输入一个2个数字用调用函数写出这2个数字的和
'''
def addition(x,y):
    return x + y
a = input()
x = int(a)
b = input()
y = int(b)
print(addition(x,y))

'''
调用函书打印出abcdef的变量所对应的数字两两计算得出的结果是第一个数字加第二个数字减去第一个数字的差
'''
def cal(x,y):
    return x + y - x
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
print(cal(a,b),cal(c,d),cal(e,f))
'''
调用函数x等于初始体重y等于每年增加的体重得出在十五年之中在地球上和月球上的体重
'''
def moon(x,y):
    h = 0
    for m in range(1,16):
        h = h + y
        print('我在第', m, '年在地球的体重', h + x, '在第', m, '年在月球的体重', (x + h) * 0.165)



a = input()
n = int(a)
b = input()
z = int(b)
moon(n,z)
'''
输入一个名字打印出你好，加上输入的名字
'''
def name(x):
    print('你好，',x)
a = input()
name(a)
'''
调用函数输入一个正方形的边长打印出他的面积
'''
def square_perimeter(x):
    return x * 4
z = input()
a = int(z)
print(square_perimeter(a))

