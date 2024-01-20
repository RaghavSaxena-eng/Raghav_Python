import random

top_of_range = input("type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number greater than 0")
        quit()
else:
    print("please type a number")
    quit()

random_number = random.randint(0, top_of_range)
guess = 0

while True:
    guess += 1
    user_guess = input("guess the number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("please enter a number next time.")
        continue

    if user_guess == random_number:
        print("You got it right!")
        break
    elif user_guess > random_number:
        print("You were above the number")
    else:
        print("you were below the number")

print("You got it in "+ str(guess) +" guesses")