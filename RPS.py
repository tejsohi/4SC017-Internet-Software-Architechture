import random


def numberToName(number):
    if number == 1:
        return "rock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "scissors"
    else:
        return "Invalid number. Program error"


def nameToNumber(name):
    if name == "rock":
        return 1
    elif name == "paper":
        return 2
    elif name == "scissors":
        return 3
    else:
        return "Invalid Name, Program error"


def main():
    user = input("Do you want to choose rock, paper or scissors?\n: ")
    userNumber = nameToNumber(user)

    compNumber = random.randint(1, 3)
    comp = numberToName(compNumber)

    results = (userNumber - compNumber) % 3

    if results == 0:
        winner = "Nobody"
    elif results == 1:
        winner = "Player 1"
    elif results == 2:
        winner = "Computer"
    else:
        winner = "Invalid winner"

    print(f"Player 1 chooses: {user}")
    print(f"Computer chooses: {comp}")
    print(f"{winner} is the winner!!")


main()
