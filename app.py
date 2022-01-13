from random import randint as ra

#start of game
print ("Guess a number between 1 and 13")

#PC picking a card
for i in range(1):
    x = ra(1, 13)

#Player guess 1
g1 = int(input())

#Checking if guess 1 is correct
if g1 == x:
    print("Correct!")
elif g1 < x:
    print("Higher!")
else:
    print("Lower!")

#if guess 1 is wrong, guess 2    
g2 = int(input())

#check if guess 2 is correct
if g2 == x:
    print("Correct!")
else:
    print("You loose!")

#print the correct answer if both guesses are wrong
if g1 and g2 != x:
    print("The number was " + str(x))