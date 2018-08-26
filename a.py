'''
输入2个数字比较大小第一个大打印第一个数大第二个数大打印第二个数大一样打印相等
'''
print('输入一个整数')
a=input()
x=int(a)
print('在输入一个整数')
b=input()
y=int(b)

if x > y:
    print('第一个数大')  
    print(x)

elif y > x:
    print('第二个数大')
    print(y) 
else:
    print('相等')