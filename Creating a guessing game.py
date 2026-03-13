secret_number = 7
guess = int(input("Guess the number:"))
if guess == secret_number:
    print("Correct! You win!")
else:
    print("Wrong guess!")