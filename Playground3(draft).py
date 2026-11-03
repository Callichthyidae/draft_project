secret_number = 7
guess = int(input("Choose a number from 1-10: "))

while guess != secret_number:
    du_doan = int(input("Guess again: "))
    if guess == secret_number:
        print("Right!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Too low!")
