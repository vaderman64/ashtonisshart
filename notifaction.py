from random import uniform
import math

randomNum = math.ceil(uniform(4, 7))

if randomNum == 5:
    computerinput2 = "rock"
elif randomNum == 6:
    computerinput2 = "paper"
else:
    computerinput2 = "scissors"


randomNum = math.ceil(uniform(0, 3))

if randomNum == 1:
    computerinput = "rock"
elif randomNum == 2:
    computerinput = "paper"
else:
    computerinput = "scissors"

print("computerinput1 has " + computerinput + "\nComputerinput2 has " + computerinput2)


# Game lines for computer 1
if computerinput2 == "rock":
    if computerinput == "rock":
        print("Its a tie!")
    if computerinput == "paper":
        print("Computerinput2 lose!")
    if computerinput == "scissors":
        print("Computerinput2 win!")
if computerinput2 == "paper":
    if computerinput == "paper":
        print("Its a tie!")
    if computerinput == "scissors":
        print("Computerinput2 lose!")
    if computerinput == "rock":
        print("Computerinput2 win!")
if computerinput2 == "scissors":
    if computerinput == "scissors":
        print("Its a tie!")
    if computerinput == "rock":
        print("Computerinput2 lose!")
    if computerinput == "paper":
        print("Computerinput2 win!")
