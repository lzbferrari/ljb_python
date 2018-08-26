#输出小于95的奇数
for x in range(1,800):
    a = x * 2 - 1
    if a == 95:
        break
    print(a)

b = 0
while b < 95:
    b = b + 1
    a = b * 2 - 1
    print(a)
    if a == 93:
        break

c = 1
while c < 95:
    a = c * 2 - 1
    if a >= 95:
        break
    print(a)
    c = c + 1