import random

i = 0
xx = []

for i in range(20):
 xx = xx + [random.randint(-20, 49)]




def func(list1):
    x = min(list1)
    result = list1.index(x)

    return result

z = func(xx)

print(z)
