'''
输入年份在地球的体重每年加1斤在月球要乘以0.165最后得出你输入的年份中的那几年在地球和月球的体重
'''
a = 50
b = input()
z = int(b)
z = z + 1
for x in range(1,200):
    if x == z:
        break
    print('我第',x,'年在月球上的体重是：',a * 0.165,'在第',x,'年我在地球上的体重：',a)
    a = a + 1
