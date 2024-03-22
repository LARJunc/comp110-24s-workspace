"""One Shot Battleship."""

__author__ = "730711502"

grid_Size: int = 4
secret_Row: int = 3
secret_Column: int = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

result: str = ""
hit: bool
# We take a guess from the user for the row.
guess_Row: int = int(input("Guess a row: "))
# If the guess for the row is out of the possible range we will enter a while loop until we get one inside of the range
if guess_Row < 1 or guess_Row > grid_Size:
    while True:
        guess_Row = int(input(f"The grid is only {grid_Size} by {grid_Size}. Try again: "))
        if guess_Row >= 1 and guess_Row <= grid_Size:
            break
        else:
            continue
# The same process will be done for the guess of the column.
guess_Column: int = int(input("Guess a Column: "))
if guess_Column < 1 or guess_Column > grid_Size:
    while True:
        guess_Column = int(input(f"The grid is only {grid_Size} by {grid_Size}. Try again: "))
        if guess_Column >= 1 and guess_Column <= grid_Size:
            break
        else:
            continue
# If both the guesses for the row and column are equal to where the battleship is then we enter this if statement
if guess_Column == secret_Column and guess_Row == secret_Row:
    hit = True
    result += RED_BOX
# if not then we enter this one.
else:
    hit = False
    result += WHITE_BOX
# We initialize a counter variable for the row.
counter_Row: int = 1
# While the counter_row variable is less than the grid size this loop will go on.
while counter_Row <= grid_Size:
    # We initialize a counter variable for the column and an emoji_box variable to store the emojis.
    counter_Column: int = 1
    emoji_Box: str = ""
    # Say that our guess row is equal to the row we are currently on this will proceed
    if guess_Row == counter_Row:
        # While the counter column is less than the grid size this will continue.
        while counter_Column <= grid_Size:
            # If out counter variable is on our guess then we will add the result to the emoji box
            if guess_Column == counter_Column:
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
if hit:
    print("Hit!")
else:
    if guess_Column == secret_Column:
        print("Close! Correct Column, wrong row.")
    elif guess_Row == secret_Row:
        print("Close! Correct row, wrong column.")
    else:
        print("Miss!")
