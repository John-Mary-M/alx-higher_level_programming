#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x integers in a list and returns the number of integers
    printed.
    """
    count = 0  # variable to keep track of the number of integers printed
    if (my_list):

        for i in range(x):  # Loop through the range from 0 to x-1
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1  # Increment the count of integers printed
            except (IndexError, ValueError, TypeError):  # If an error occurs
                break  # Exit the loop
    print()  # Print a newline character after all the integers are printed
    return count  # Return the count of integers printed
