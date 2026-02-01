import random


def choose_difficulty():
    """
    Ask the player to choose a difficulty level.
    Returns: (max_number, attempts)
    """
    print("\nChoose difficulty:")
    print("1) Easy   (1-10,   5 attempts)")
    print("2) Medium (1-50,   7 attempts)")
    print("3) Hard   (1-100, 10 attempts)")

    while True:
        choice = input("Your choice (1/2/3): ").strip()

        if choice == "1":
            return 10, 5
        if choice == "2":
            return 50, 7
        if choice == "3":
            return 100, 10

        print("Please choose 1, 2, or 3.")


def read_int_in_range(min_value, max_value):
    """
    Read an integer from the user and ensure it's within [min_value, max_value].
    Keeps asking until valid input is provided.
    """
    while True:
        raw = input(f"Enter a number between {min_value} and {max_value}: ").strip()

        try:
            number = int(raw)
        except ValueError:
            print("That is not a valid integer. Try again.")
            continue

        if min_value <= number <= max_value:
            return number

        print(f"Number must be between {min_value} and {max_value}.")


def play_round():
    """
    Play one round of the guessing game.
    Returns a round score (simple scoring system).
    """
    max_number, attempts = choose_difficulty()
    min_number = 1
    secret = random.randint(min_number, max_number)

    print(f"\nI picked a number between {min_number} and {max_number}.")
