import random 
import art
from replit import clear
EASY = 10 
HARD = 5
logo = art.logo
print(logo)
NUMBER = random_number = random.randint(1,100)
def play_number_game():
    """ This is a fucntion that runs the whole game"""
    def your_score(level):
        """ this is a function that gets the 
            difficulty_level and retuns whether the 
            user picked easy or hard. """
        if level == "easy":
            return EASY 
        elif level == "hard":
            return HARD 
        else:
            pass
    def guess_number(your_score): 
        """ This function gets the user input and compares the input to the random number""" 
        while EASY != 0 or HARD != 0:
            print(f"You have {your_score} attempts to guess the number ")
            user_guess= int(input("Make a guess: "))
            if user_guess > NUMBER:
                print("Your number is too high")
                print("guess again")
                your_score = your_score -1
            elif user_guess < NUMBER:
                print("Your number is too low")
                print("guess again")
                your_score = your_score - 1
            elif user_guess == NUMBER:
                print(f"You guessed right, The answer was {NUMBER}")
                break


    print(NUMBER)
    difficulty_level = input("Please pick your difficulty_level: 'easy' or 'hard':  ")
    #print(f"You have {easy} attempts to guess the number ")
    user_attempts=your_score(difficulty_level)
    guess_number(user_attempts)
play_again = input("Would you like to play again?: ")
if play_again == 'y':
    clear()
    play_number_game()
else:
    print("Goodbye")
