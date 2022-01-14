import random

#PC picking a card
x = random.randint(1, 13)

for i in range(2):
    g1 = 99
    #Checking player guess validity
    while ((type(g1) != int) or g1 > 13 or g1 < 1):
        try:
            print ("Guess a number between 1 and 13")
            g1 = int(input())
        except ValueError:
            print("Only numbers!")

    #Checking if guess is correct
    if g1 == x:
        print("Correct!")
        break
    elif i == 0:
        if g1 < x:
            print("Higher!")
        else:
            print("Lower!")

#print the correct answer if both guesses are wrong
if g1 != x:
    print("The number was " + str(x))