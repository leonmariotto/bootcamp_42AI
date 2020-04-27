import sys
import random

print("This is an interactive guessing game!")
print("You have to enter a number between 1 \
and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good Luck cow-boy")

goal = random.randint(1, 99)
c = 0
while 1:
    c += 1
    print("What's your guess between 1 and 99 ?")
    try:
        i = input()
    except ValueError:
        print("Error", file=sys.stderr)
        continue
    if (i == "exit"):
        print("Goodbye!")
        sys.exit()
    try:
        n = int(i)
    except ValueError:
        print("That's not a number.")
        continue
    if n < goal:
        print("Too low !")
    elif n > goal:
        print("Too high !")
    else:
        print("Congratulations, you've got it!")
        print("You won in", c, "attempts!")
        sys.exit()
