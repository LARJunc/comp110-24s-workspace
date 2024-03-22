"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730711502"

# emojis
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


# Checking the appropriate 'size' of location
secret_boat_location_player1: int = int(input("Pick a secret boat location between 1 and 4: "))
if secret_boat_location_player1 > 4:
    print(f"Error! {secret_boat_location_player1} is too high!")
    exit()
elif secret_boat_location_player1 < 1:
    print(f"Error! {secret_boat_location_player1} is too low!")
    exit()
# Checking the appropriate 'size' of guess
player2_guess: int = int(input("Guess a number between 1 and 4: "))
if player2_guess > 4:
    print(f"Error! {player2_guess} is too high!")
    exit()
elif player2_guess < 1:
    print(f"Error! {player2_guess} is too low!")
    exit()
result: str
statement: bool
# set result to RED if correct and WHITE if wrong
if secret_boat_location_player1 == player2_guess:
    result = RED_BOX
    statement = True
else:
    result = WHITE_BOX
    statement = False
# append each corresponding box to output string
output: str = ""
if player2_guess == 1:
    output += result
else:
    output += BLUE_BOX
if player2_guess == 2:
    output += result
else:
    output += BLUE_BOX
if player2_guess == 3:
    output += result
else:
    output += BLUE_BOX
if player2_guess == 4:
    output += result
else:
    output += BLUE_BOX
print(output)
if statement:
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")
