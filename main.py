print('-----------------Game----------------')
import random

counts = 3
score = 0
while score < 3:
    answer = random.randint(1, 10)
    while counts > 0:
        temp = input("can you guess a number between 1-10:")
        guess = int(temp)
        if guess == answer:
            print("what the fucking lucky")
            print("you are right")
            score = score + 1
            counts = 3
            break
        else:
            if guess < answer:
                print("is small")
            else:
                print("is big")
            counts = counts - 1
        if counts < 1:
            print("what a pity")
            print("the number is " + str(answer))
            counts = 3
            break

print("game over")
print("Do you like this game?")
review = input("yes/no:")
if review == "yes":
    print("Thank you")
if review == "no":
    print(" F**K YOU\n " * 100)
print("Thank you for your evaluation")
input("Press ANY-KEY to exit game")




