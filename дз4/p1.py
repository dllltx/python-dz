while True:
    print("Welcome to a text game")
    print("\nyou see a girl, what's your next action?")
    choice = input("\n1. kiss her\n2. tell her she's beautiful\n3. ignore her\n")

    if choice == "1":
        print("you just kissed a random girl you saw")
        print(
            "\nGirl: EW, WTF ARE YOU DOING????\nThe girl called the cops on you\nCops: Sir, put your hands behind your back now! You're under arest for assaulting the girl!")
        choiceone = input(" |GAME OVER|\n1. Try again?\n2. Exit\n")
        if choiceone == "2":
            print("Goodbye!")
            break
        elif choiceone != "1":
            print("nuh uh buddy, game over for you")
            break

    elif choice == "2":
        print(
            "you just told a random girl that she's beautiful\n the girl seemed to find you not so bad either\nGirl: hmmm, i kinda like that, here's my phone number - *gives you her phone number*")
        print("*5 years later*\n you're now a happy husband with your beautiful wife and kids, congrats buddy")
        choicetwo = input(" |GAME OVER|\n1. Try again?\n2. Exit\n")
        if choicetwo == "2":
            print("Goodbye!")
            break
        elif choicetwo != "1":
            print("nuh uh buddy, game over for you")
            break

    elif choice == "3":
        print("You decided to ignore the girl")
        print(
            "\nyou just lost your chance to have a great girlfriend or a friend... or was it worth it? who knows, maybe she's actually THE DEVIL HERSELF")
        choicethree = input(" |GAME OVER|\n1. Try again?\n2. Exit\n")
        if choicethree == "2":
            print("Goodbye!")
            break
        elif choicethree != "1":
            print("nuh uh buddy, game over for you")
            break

    else:
        print("Invalid choice! Please select 1, 2 or 3.")
        