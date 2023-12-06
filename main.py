import random
import keyboard
import datetime as dt

NOTATIONS = ["R", "U", "L", "D", "F", "B"]   # Cube move/direction
SUFFIXES = ["", "'", "2"]                    # Clockwise, Counterclockwise, Twice


def scrambler():
    scramble = generate_scramble()
    return '  '.join(f"{move[0]}{move[1]}" for move in scramble)    # Returns scramble into single string


def generate_scramble():
    length = random.randint(25, 28)
    scramble = []

    for _ in range(length):
        move = (random.choice(NOTATIONS), random.choice(SUFFIXES))

        # Validating function to avoid repetitions
        while scramble and (move[0] == scramble[-1][0] or (len(scramble) >= 2 and move[0] == scramble[-2][0])):
            move = (random.choice(NOTATIONS), random.choice(SUFFIXES))

        scramble.append(move)

    return scramble


def timer():  # Time it takes to solve scramble
    print("\nPress the Space key to begin solve...\n")
    keyboard.wait("space")
    start = dt.datetime.now()
    print("Press the Space key to end solve...\n")
    keyboard.wait("space")
    end = dt.datetime.now()

    solve_time = (end - start).total_seconds()
    print(f"Time: {solve_time:.3f}")


print("Press Enter to begin generating scrambles...")

while True:  # Loops scramble and timer
    keyboard.wait("enter")  # Press Enter to generate new scramble
    print("\nScramble:\n", scrambler())
    timer()
    print()
