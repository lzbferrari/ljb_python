'''
输入一个数字打印出这是第h次循环h = 你输入的年份打印出到这个年份为止的所有数字
'''


def circulation2(a):
    h = 1
    while h <= a:
        print('这是第', h, '次循环')
        h = h + 1


b = input()
c = int(b)
circulation2(c)
