# a = abs(10) + abs(-10)
# print(a)
# b = abs(-10) + -10
# print(b)

'''
复制文件，将一个文件中的内容复制到另一个文件中，复制看emm.txt和test.txt
'''

b = open('D:\\code\\python\\ljb\\emm.txt\\test.txt')
d = b.read()

print(d)
a = open('D:\\code\\python\\ljb\\emm.txt\\eeeeee.txt','w')
c = a.write(d)
a.close()
z = open('D:\\code\\python\\ljb\\emm.txt\\eeeeee.txt')
n = z.read()
print(n)








# a = 'this if is you not are a reading very this good then way you to have hide done a it message wrong'
# b = a.split()
# for c in b:
#     print(c)
