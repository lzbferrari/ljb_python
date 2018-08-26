'''
将列表中的单词打印出来并在前面打出数字12345一一对应的
'''
ingredient = ['snails','leeches','gorilla belly-button lint','caterpillar eyebrows','centipede toes']
b = 1
for a in ingredient:
    print(b,a)
    b = b + 1


'''
输出将123456打印成
123
234
345
456
'''
a = [1,2,3,4,5]
for b in a:
    x = b + 1
    v = b + 2
    print(b * 100 + x * 10 + v)