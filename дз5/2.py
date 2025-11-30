num = 5


def search(num):
    if num == 0:
        return [[]]

    combinations = []

    for i in range(1, num + 1):
        for comb in search(num - i):
            combinations.append([i] + comb)

    return combinations


result = search(num)
for comb in result:
    print(comb)