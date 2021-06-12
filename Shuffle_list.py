from random import shuffle


def suffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():

    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Pick a number 0,1 or 2: ")

    return int(guess)


def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print("Correct !!")
    else:
        print("Wrong Guess !!")


mylist = ['','0','']

mixed_list = suffle_list(mylist)

guess = player_guess()

check_guess(mixed_list,guess)
