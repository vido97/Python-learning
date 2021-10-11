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
    
    while guess != right_number and guesses_left > 0:
        guesses_left = guesses_left -1

        if guesses_left == 0 :
            print ("KABOOM!\nYou didn't find the right number in time and the bomb exploded.")

        if guess < MIN_NUMBER  or guess > MAX_NUMBER:
            print("The number is between", MIN_NUMBER , " and ", MAX_NUMBER)

        elif guess > right_number:
            print("The number is smaller.")

        elif guess < right_number:
            print("The number is bigger.")

        if guesses_left == 1:
            print ("You have 1 guess left!")

        guess = int(input("Enter the next guess:\n"))
        
    if guess = right_number and guess_left > 0 :
        print("You found the right number in time!")
        
    print(f"The right number was {right_number:d}")

main()
