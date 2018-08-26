# import copy
# class Car:      #第一题
#     pass
# car1 = Car()
# car1.wheels = 4
# car2 = car1
# car2.wheels = 3
# print(car1.wheels)
# car3 = copy.copy(car1)
# car3.wheels = 6
# print(car1.wheels)


'''
将一个内容用python放入一个文件并且在python中打印出来
'''
import pickle
a = ['beef']
b = open('D:\\code\\python\\ljb\\ten\\favirites.dat','wb')
pickle.dump(a,b)
b.close()
load_e = open('D:\\code\\python\\ljb\\ten\\favirites.dat','rb')
p = pickle.load(load_e)
load_e.close()

print(p)
