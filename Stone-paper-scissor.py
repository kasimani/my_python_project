import random
#from random import shuffle

#def suffle_list(computeroption):
#    shuffle(computeroption)
#    return computeroption[0]


def player_userchoice():
    userchoice = ''
    while userchoice not in ['stone','paper','scissor']:
        userchoice = input("Enter either Stone or Paper or Scissor:\n")

    return userchoice


def decission(userchoice,compterchoice):
    print ("User-Choice = " + userchoice + " Computer-choice = " + compterchoice)
    if compterchoice == "paper" and userchoice == "stone":
        print("Computer Wins !!\n")
    elif compterchoice == "scissor" and userchoice == "paper":
        print("Computer Wins !!\n")
    elif compterchoice == "stone" and userchoice == "scissor":
        print("Computer Wins !!\n")
    elif (compterchoice == "stone" and userchoice == "stone") or (compterchoice == "paper" and userchoice == "paper") or (compterchoice == "scissor" and userchoice == "scissor"):
        print("Draw\n")
    else:
        print("You Win\n")

#compterchoice = suffle_list(computeroption)

while True:
    computeroption = ['stone','paper','scissor']
    compterchoice = random.choice(computeroption)
    userchoice = player_userchoice()
    #print(f"Human {compterchoice}")
    decission(userchoice,compterchoice)
    play_again = input("Want to play again? (Y/N)")
    if play_again.lower() != "y":
        break