#!/usr/bin/env python3
# Created By: Lennon Cehajic
# Date: October 15th, 2026
# This program runs a random number guessing game.
import constants


def main():
    # Get the guessed number from the user.
    user_guess = int(input("Guess a number between 0 and 9: "))

    # Check if the guessed number is equal to the correct number.
    if user_guess == constants.CORRECT_NUMBER:
        print("You have guessed correctly!")

    if user_guess != constants.CORRECT_NUMBER:
        print("You have guessed incorrectly!")


if __name__ == "__main__":
    main()
