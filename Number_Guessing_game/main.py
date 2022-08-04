# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


def check_answer(actual, guess, turn):
    if guess > actual:
        print("Too high")
        return turn - 1
    elif guess < actual:
        print("Too low")
        return turn - 1
    else:
        print(f"you've got it. The answer was {actual}")


easy_level_turn = 10
hard_level_turn = 5


def set_difficulty():
    """according to difficulty level return turns"""
    level = input('Choose a difficulty. Type "easy" or "hard": ')
    if level == 'easy':
        return easy_level_turn
    elif level == 'hard':
        return hard_level_turn


import random


# game starting here
def game():
    print("Welcome to number guessing game")
    print("I'm thinking of a number between 1 and 100")

    # choosing a random number between 1 and 100
    actual_number = random.randint(1, 100)
    # print(f"The correct answer is {actual_number}")

    # getting the no of turns according to difficulty level
    turn = set_difficulty()
    # print(f"you have {turn} attempts remaining to guess the number")

    guess = 0
    # compare guess & actual answer
    while guess != actual_number:
        print(f"you have {turn} attempts remaining to guess the number")
        # make my guess
        guess = int(input("make a guess: "))
        turn = check_answer(actual_number, guess, turn)

        # tracking turn and decreasing it every time
        # turn -= 1
        # print(f"you have {turn} attempts remaining to guess the number")
        """
         you've got it. The answer was 70
         you have 3 attempts remaining to guess the number
         """
        # in this case if the user wins also it would keep tracking

        # need to give a condition so that while loop ends. and it ends when num of turns = 0
        if turn == 0:
            print("You've run out of guesses, you lose.")
            return  # would throw SyntaxError: 'return' outside function


"""
How do I fix error "return outside function" in Python?
To resolve the return outside function SyntaxError in Python, create a function and write the loop inside that function, and then use the return function. This is the correct way to use the return.
"""
game()