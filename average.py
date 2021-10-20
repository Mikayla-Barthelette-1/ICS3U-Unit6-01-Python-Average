#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program calculates the average of 10 random numbers

import random

import constants


def main():
    # this function calculates the average

    random_numbers = []
    the_sum = 0

    # input
    print("Starting ...")
    print("")

    # process
    for loop_counter in range(0, 10):
        a_random_number = random.randint(1, 100)  # a number between 1 and 100
        random_numbers.append(a_random_number)
        print("The random number is: {0}".format(random_numbers[loop_counter]))

    for loop_counter in range(0, 10):
        the_sum = the_sum + (random_numbers[loop_counter])
        average = the_sum / constants.AMOUNT_OF_NUMBERS

    print("\nThe average is {0}.".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
