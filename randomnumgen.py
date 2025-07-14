import random

def guess_the_number():
    """Plays a 'guess the number' game."""
    secret_number = random.randint(1, 100)
    totalAttempts = 0
    
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            totalAttempts += 1

            if (guess < secret_number):
                print("too low")
            elif (guess > secret_number):
                print("too high")
            else:
                print(f"wow! you guessed the number {secret_number} in {totalAttempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
