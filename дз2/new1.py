def func(a, b):
    list1 = range(a, b)
    list2 = []
    for x in list1:
        if x % 2 != 0:
            list2.append(x)

    if a in list2:
        list2.remove(a)

    return list2

blablallba= func(1, 31)
print(blablallba)