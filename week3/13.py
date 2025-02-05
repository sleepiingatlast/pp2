import random

def guess_game():
    name = input("Hello! What is your name? ")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    
    secret = random.randint(1, 20)
    num_of_guesses = 0
    
    while True:
        tells_to_guess = input("Take a guess ")
        
        if tells_to_guess.isdigit():
            guess = int(tells_to_guess)
            num_of_guesses += 1
            
            if guess < secret:
                 print("Your guess is too low.")
            elif guess > secret:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {num_of_guesses} guesses!")
                break
        else:
            print("That's not a number! Try again.")

guess_game()