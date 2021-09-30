import random

def main():
    MIN_NUMBER = 0
    MAX_NUMBER = 1000
    MIN_GUESSES = 7
    MAX_GUESSES = 20

    # Generate the random number and the number of guesses
    seed_number = int(input("Enter a seed:\n"))
    random.seed(seed_number)
    right_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    guesses_left = random.randint(MIN_GUESSES, MAX_GUESSES)

    guess = int(input("Enter your guess:\n"))
    guess_count = 1

    while guess_count >=0:

        if guess == right_number:
            print(f"You found the right number in time!\nThe right number was {right_number:d}.")
            break

        if guess_count == guesses_left:
            print (f"KABOOM!\nYou didn't find the right number in time and the bomb exploded.\nThe right number was {right_number:d}.")
            break

        if guess <0 or guess >1000:
            print("The number is between 0 and 1000.")

        elif guess > right_number:
            print("The number is smaller.")

        elif guess < right_number:
            print("The number is bigger.")

        if guess_count==guesses_left-1:
            print ("You have 1 guess left!")

        guess = int(input("Enter the next guess:\n"))

        guess_count += 1
main()
