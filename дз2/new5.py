def blalbal(a):
    if a < 2:
        return False
    for x in range(2, a):
        if a % x == 0:
            return False
    return True

print(blalbal(7))
