'''
调用三个函数一个用来计算Y列表中最大的数最小的数第二个用来计算x列表中最大的数字和最小的数字第三个用来将y和x列表中的最大最小的数字打印出来
'''
def my_max(a):
    maxa = 3
    for b in a:
        if b > maxa:
            maxa = b
    return maxa

def my_min(a):
    mina = 100
    for s in a:
        if s < mina:
            mina = s
    return mina

def my_print(maxa, mina):
    print('最大值是：',maxa)
    print('最小值是：',mina)


y = (3,69,52,8,5,4,9,7)
maxyyy = my_max(y)
minyyy = my_min(y)
my_print(maxyyy, minyyy)


x = (3,3,80,8,5,1,9,7)
maxxx = my_max(x)
minxx = my_min(x)
my_print(maxxx, minxx)