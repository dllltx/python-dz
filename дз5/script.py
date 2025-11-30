list = [1, 3, 5, 84, 8, 17]


def search(list):
    if len(list) == 1:
        return list[0]

    max = search(list[1:])

    return list[0] if list[0] > max else max


max_num = search(list)
print(max_num)