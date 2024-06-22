# generate a number
# take input from user
# Check if that input is a number in the asked range
# check if the input is the right guess. Otherwise ask again


from random import randint

answer = randint(1, 10)


while True:
    try:
        guess = int(input("Guess the number: "))
        if 0 < guess < 11:
            if guess == answer:
                print("You guessed the right number!")
                break
            else:
                print("wrong!")
        else:
            print("please enter number between 1 and 10")
    except ValueError:
        print("please enter a number")
