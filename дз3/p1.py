import random
#СПУСТЯ 2 ЧАСА ТУПИЗМА И ОБЪЯСНИТЕЛЬНОЙ БРИГАДЫ НЕЙРОНКИ Я ЧЕ ТО СДЕЛАЛ ВРОДЕ
def password(length, special_symbols, capital_letters, non_cap_letters, numbers):
    password = ""
    result = list(special_symbols + capital_letters + non_cap_letters + numbers)
    for i in range(length):
        password += random.choice(result)
    def pass_check(password):
        if len(password) < 8:
            print("your pass is too short")
        elif not any(x in special_symbols for x in password) and not any(
                x in capital_letters for x in password) and not any(x in numbers for x in password):
            print("ABSOLUTE GARBAGE DUDE, add special symbols or capital letters or numbers")
        elif not any(x in capital_letters for x in password) and (
                any(x in numbers for x in password) or any(x in special_symbols for x in password)):
            print("good pass, but i'd advice to add some capital letters")
        elif not any(x in special_symbols for x in password):
            print("no special symbols is bad dude, bad password")
        elif not any(x in numbers for x in password):
            print("ok pass but add numbers")
        else:
            print("nice one")
    pass_check(password)
    return password

x = password(9, "*!$", "AFV", "acbef", "124124")
print(x)
