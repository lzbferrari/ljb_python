'''
调用函数输入初始体重，每年增加的体重，要计算几年打印出输入的年份中的每一年在地球上和月球上的体重
'''
def moon(x,y,o):
    h = 0
    for m in range(1,2000000):
        if o == m:
            break
        h = h + y
        print('我在第', m, '年在地球的体重', h + x, '在第', m, '年在月球的体重', (x + h) * 0.165)

a = input()
n = int(a)
b = input()
z = int(b)
q = input()
v = int(q)
moon(n,z,v)