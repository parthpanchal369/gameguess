from random import shuffle

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list

my_list = [' ','O',' ']

def player_guess():
    guess = ' '

    while guess not in ['0','1','2']:

        guess = input("Enter your guess here: 0, 1, or 2 ")

    return int(guess)

def check_guess(mylist,guess):

    if mylist[guess] == 'O':
        print('You Guess Correct')

    else:
        print("!Sorry Wrong Guess")
        print(my_list)


# INIAL LIST
mylist = [' ','O',' ']

#SHUFFLE LIST
mixed_list = shuffle_list(mylist)

# USER GUESS
guess = player_guess()

# CHECK GUESS
check_guess(mixed_list,guess)