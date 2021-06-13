import random
from random import shuffle

def suffle_list(computeroption):
    shuffle(computeroption)
    return computeroption[0]


def player_userchoice():

    userchoice = ''
    while userchoice not in ['Stone','Paper','Scissor']:
        userchoice = input("Enter either Stone or Paper or Scissor:\n")

    return userchoice



def decission(compterchoice,userchoice):
    print ("User-Choice = " + userchoice + " Computer-choice = " + compterchoice)
    if compterchoice == "paper" and userchoice == "Stone":
        print("Computer Wins !!")
    elif compterchoice == "scissor" and userchoice == "Paper":
        print("Computer Wins !!")
    elif compterchoice == "stone" and userchoice == "Scissor":
        print("Computer Wins !!")
    elif (compterchoice == "stone" and userchoice == "stone") or (compterchoice == "Paper" and userchoice == "Paper") or compterchoice == "Scissor" and userchoice == "Scissor":
        print("Draw")
    else:
        print("You Win")



computeroption = ['stone','paper','scissor']
compterchoice = suffle_list(computeroption)
#compterchoicerandom = random.choice(computeroption)
#print(compterchoicerandom)
userchoice = player_userchoice()
decission(compterchoice,userchoice)
