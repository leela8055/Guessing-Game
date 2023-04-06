# Leela Achanta_3141735.py
# Leela Achanta(3141735)
# Guess the number game
# Homework
# April 2, 2023
"""
Module to generate a random number between 1 and 100, and ask the user to guess the number.
The program will provide feedback to the user on whether their guess was too high or too low,
and keep track of the number of guesses it took the user to find the correct answer.
"""
from random import *  # Extracts all the functions of random
import logic
for m in range(1, 1000):  # loop for repeating the game 1000 times once started
    x = randint(1, 100)  # Creating a random variable
    logic.conditions(x)
