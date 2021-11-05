import random

lower_bound = 1
upper_bound = 100

number = random.randint(lower_bound, upper_bound)
print ("I have picked a number between", lower_bound, "and", upper_bound, "(inclusive). Can you guess it?")
guess = int(input("Please enter your guess > "))
while guess != number:
    if guess < number:
        print ("increase your number")
    else:
        print ("decrease your number")
    
    guess = int(input("Your guess > "))

print ("Congratulations! You have found the correct number!")