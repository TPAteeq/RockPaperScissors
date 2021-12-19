import random

while True:
    choices = ['rock','paper','scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors? :").lower()

    if player == computer:
        print("computer :",computer)
        print("player :",player)
        print("Tie")

    elif player == "rock":
        if computer == "paper":
            print("computer :", computer)
            print("player :", player)
            print("you lose")
        elif computer == "scissors":
            print("computer :", computer)
            print("player :", player)
            print("you win")

    elif player == "paper":
        if computer == "rock":
            print("computer :", computer)
            print("player :", player)
            print("you win")
        elif computer == "scissors":
            print("computer :", computer)
            print("player :", player)
            print("you lose")

    elif player == "scissors":
        if computer == "paper":
            print("computer :", computer)
            print("player :", player)
            print("you win")
        elif computer == "rock":
            print("computer :", computer)
            print("player :", player)
            print("you lose")

    play_again = input("play again?(y/n): ").lower()

    if play_again !="y":
        break

print("bye!")
