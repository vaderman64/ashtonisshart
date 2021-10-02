from random import uniform
import math
userinput = input("choose rock paper or scissor:  ")

randomNum = math.ceil(uniform(0, 3))

if randomNum == 1:
    computerinput = "rock"
elif randomNum == 2:
    computerinput = "paper"
else:
    computerinput = "scissors"


# Game lines
if userinput == "rock":
    if computerinput == "rock":
        print("Its a tie!")
    if computerinput == "paper":
        print("You lose!")
    if computerinput == "scissors":
        print("You win!")
if userinput == "paper":
    if computerinput == "paper":
        print("Its a tie!")
    if computerinput == "scissors":
        print("You lose!")
    if computerinput == "rock":
        print("You win!")
if userinput == "scissors":
    if computerinput == "scissors":
        print("Its a tie!")
    if computerinput == "rock":
        print("You lose!")
    if computerinput == "paper":
        print("You win!")
