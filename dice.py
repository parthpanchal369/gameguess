import random

asking = input("Enter your input:  Y/n  ")

while asking == 'y':
    num = random.randint(1,6)

    if num == 1:
        print(1)

    elif num == 2:
        print(2)

    elif num == 3:
        print(3)

    elif num == 4:
        print(4)

    elif num == 5:
        print( 5)

    else:
        print(6)

    asking = input("Enter your input:  Y/n  ")

    if asking == 'n':
        break 