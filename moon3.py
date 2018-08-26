'''
调用函数只是比moon2.py更加的好要输入的时候增加的输入初始体重，输入没每年增长几斤，输入要计算几年
'''
def moon_weight():
    print('输入初始体重')
    a = input()
    b = int(a)
    print('输入每年增长几斤')
    c = input()
    d = int(c)
    print('输入要计算几年')
    e = input()
    f = int(e)
    h = 0
    for m in range(1,2000000):
        if f == m:
            break
        h = h + d
        print('我在第', m, '年在地球的体重', h + b, '在第', m, '年在月球的体重', (b + h) * 0.165)
print(moon_weight())
