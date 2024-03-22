"""Functional battleship."""

__author__ = "730711502"


import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(grid_Size: int, spec: str) -> int:
    """Input guess function."""
    # What the following function does is it takes in 2 arguments. A grid size and the specification for their guess.
    assert spec == "row" or spec == "column"
    # We ask the user to make a guess for their row/column.
    guess: int = int(input(f"Guess a {spec}: "))
    # Depending on if their guess is out of the possible range we will enter the following while loop.
    if guess < 1 or guess > grid_Size:
        # Continue asking the user for a new guess until it is final within the possible range.
        while True:
            guess = int(input(f"The grid is only {grid_Size} by {grid_Size}. Try again: "))
            if guess >= 1 and guess <= grid_Size:
                return guess
            else:
                continue
    return guess
    # Return their guess.


def print_grid(grid_Size: int, row_Guess: int, column_Guess: int, user_Result: bool) -> None:
    """Print grid function."""
    result: str = ""
    if user_Result:
        result += RED_BOX
    # if not then we enter this one.
    else:
        result += WHITE_BOX
    # We initialize a counter variable for the row.
    counter_Row: int = 1
    # While the counter_row variable is less than the grid size this loop will go on.
    while counter_Row <= grid_Size:
        # We initialize a counter variable for the column and an emoji_box variable to store the emojis.
        counter_Column: int = 1
        emoji_Box: str = ""
        # Say that our guess row is equal to the row we are currently on this will proceed
        if row_Guess == counter_Row:
            # While the counter column is less than the grid size this will continue.
            while counter_Column <= grid_Size:
                # If out counter variable is on our guess then we will add the result to the emoji box
                if column_Guess == counter_Column:
                    emoji_Box += result
                    counter_Column += 1
                # If not then we will just add a blue box.
                else:
                    emoji_Box += BLUE_BOX
                    counter_Column += 1
    # For any other scenario we will just add a blue box
        else:
            while counter_Column <= grid_Size:
                emoji_Box += BLUE_BOX
                counter_Column += 1
        # After we are done with adding boxes to the emojibox variable then we will increase the counter_row by one and print out the row of emoji boxes.
        counter_Row += 1
        print(emoji_Box)


def correct_guess(secret_Row: int, secret_Column: int, guess_Row: int, guess_Column: int) -> bool:
    """Correct guess function."""
    # The following function takes in the secret row and column and the user's guess.
    if guess_Row == secret_Row and guess_Column == secret_Column:
        return True
    else:
        return False
    

def main(grid_Size: int, secret_Row: int, secret_Column: int) -> None:
    """Main function."""
    # What this function does it takes all of the functions from before and forms it into a cohesive game.
    turn_Counter: int = 1
    victory: bool = False
    # The game runs until the user is out of turns or finally guesses it correctly.
    while turn_Counter <= 5 and victory is False:
        print(f"=== Turn {turn_Counter}/5 ===")
        row_Guess: int = input_guess(grid_Size, "row")
        column_Guess: int = input_guess(grid_Size, "column")
        result: bool = correct_guess(secret_Row, secret_Column, row_Guess, column_Guess)
        print_grid(grid_Size, row_Guess, column_Guess, result)
        if result:
            print("Hit!")
            print(f"You won in {turn_Counter}/5 turns!")
            victory = True
        else:
            print("Miss!")
            turn_Counter += 1
    print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))
        
