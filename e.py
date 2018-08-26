'''
调用函数打印出一年内你在地球的体重和在月球的体重
'''
def ljb_power(x):
    z = x * 0.165
    return z


a = input()
b = int(a)

y = ljb_power(b)

print('your earth weight is',b,'kg','your moon weight is',y)