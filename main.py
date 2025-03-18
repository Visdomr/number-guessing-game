import random

print("Welcome to Guess the Number Game!")

number = random.randint(1, 101)

tries = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 100: "))

        tries += 1
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100 only.")

        elif guess == number:
            print("You guessed correctly in: ", tries, "tries!")
            print("Winning guess was: ", guess)
            play_again = input(
                "Would you like to continue playing? yes/no, y/n: ").lower()
            if play_again == "y" or play_again == "yes":
                number = random.randint(1, 101)
                tries = 0

            elif play_again == "n" or play_again == "no":
                print("Thanks for playing! Goodbye.")
                break
            else:
                print("Please enter yes or no, y or n only.")

        if guess > number:
            print("Your guess is too high.")
        elif guess < number:
            print("Your guess is too low.")
    except ValueError:
        print("Please enter a number between 1 and 100 only.")
