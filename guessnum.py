import random 

x = random.randrange(1,10)

user = int(input("Guess a number between 1 and 10: "))
while user != x:
    user = int(input("Guess a number between 1 and 10: "))

print("You guessed it")





BEGIN
    IMPORT random

    x = random number between 1 and 10

    user = INPUT("Guess a number between 1 and 10: ")

    WHILE user is NOT equal to x DO
        user = INPUT("Guess a number between 1 and 10: ")
    END WHILE

    PRINT "You guessed it"
END