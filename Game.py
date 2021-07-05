#rock-papar-scissor-game
import random

items = ["rock", "paper", "scissor"]

your_move = str(input("choose rock, paper, or scissor"))
computer_move = random.choice(items)

print("computer chooses", computer_move)

if (your_move == computer_move):
    print("draw")
else:
    if((your_move == "rock" and computer_move == "scissor") or (your_move == "paper" and computer_move == "rock") or (your_move == "scissor" and computer_move == "paper")):
        print("you win")
    else:
        print("you lose")

