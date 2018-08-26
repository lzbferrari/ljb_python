'''
一个循环会打印hello x    x = 数字列表1到20如果x等于9那么就会停下来
'''
for x in range(0,20):
    print('hello %s' % x)
    if x < 9:
        break