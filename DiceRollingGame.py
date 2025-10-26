import random
input("It is Ali's turn: ")
player1 = random.randint(1, 6)
print("Ali Turn: ",player1)

input("It is Ahmed's Turn: ")
player2 = random.randint(1, 6)
print("Ahmed Turn: ",player2)

if player1 > player2:
    print("Congratulations Ali  You won!")
else:
    print("Congratulations Ahmed You won!")

