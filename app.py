from random import randint as ra

print ("Guess a number between 1 and 13")

for i in range(1):
    x = ra(1,13)

g1 = int(input())


if g1 == x:
    print("Correct!")
elif g1 < x:
    print("Higher!")
else:
    print("Lower!")
    
g2 = int(input())

if g2 == x:
    print("Correct!")
else:
    print("You loose!")

print("It was " + str(x))