import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")
    
    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Run the game
number_guessing_game()

OUTPUT:-
I have selected a number between 1 and 100. Can you guess it?
Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: 63
Too low! Try again.
Enter your guess: 70
Congratulations! You guessed it in 4 attempts.
