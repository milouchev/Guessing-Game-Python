#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:37:09 2022

@author: milouchev
"""

import random

# Building the game where the computer guesses the user's number
def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print (f"\nThe computer guessed your number {guess} correctly!")

# Building the game where the user guesses the computer's number
def guess (x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("\nSorry, guess again. Too low.")
        elif guess > random_number:
            print("\nSorry, guess again. Too high.")
    print(f"\nCongratulations. You've correctly guessed the number {random_number}.")

# Selecting the game
print("\nEnjoy this guessing game where either you will be guessing the computer's number,"+\
      " or the computer will be guessing your number.")
game = str(input("Will you be guessing the number? If yes, enter 'yes'. If no, enter 'no':  "))
if game == 'yes' or game == 'Yes' or game == 'YES':
    guess(100)
else:
    print("\nThink of a number from 1-100...")
    computer_guess(100)
