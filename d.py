'''
打印出列表中的大于或等于六小于10的数字
'''
bas = [1,5,6,2,3,8,11,13,9,20,7,17,15,1]
for ba in bas:
    if ba < 6:
        continue
    elif ba >= 6 and ba < 10:
       print(ba)
    elif ba < 15 and ba > 10:
        continue
    else:
        break
                