import random

'''
1  for snake
-1 for water
0  for gun
'''

computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (s, w, g): ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

# By know you have 2 numbers (variables), you and computer

print(f"You choose {reverseDict[you]}")
print(f"Computer choose {reverseDict[computer]}")

if (computer == you):
    print("It's a draw!")

elif (computer == -1 and you == 1):
    print("You Win!")

elif (computer == -1 and you == 0):
    print("You Lose!")

elif (computer == 1 and you == -1):
    print("You Lose!")

elif (computer == 1 and you == 0):
    print("You Win!")

elif (computer == 0 and you == -1):
    print("You Win!")

elif (computer == 0 and you == 1):
    print("You Lose!")

else:
    print("Something went wrong!")
