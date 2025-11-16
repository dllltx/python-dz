def func(lend, direction, symbol):
    if direction == "vertical":
        for i in range(lend):
            print(symbol)
    elif direction == "horizontal":
        i = symbol * lend
        print(i)
    else:
        print("error")

    return i

x = func(12, "horizontal", "#")