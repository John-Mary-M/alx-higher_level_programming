#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x integers in a list and returns the number of integers
    printed.
    """
    count = 0  # variable to keep track of the number of integers printed
    for i in range(x):  # Loop through the range from 0 to x-1
        try:
            if isinstance(my_list[i], int):  # Chk if elemnt at idx i is an int
                print("{:d}".format(my_list[i]), end="")
                count += 1  # Increment the count of integers printed
        except IndexError:  # If an IndexError occurs
            break  # Exit the loop
    print()  # Print a newline character after all the integers are printed
    return count  # Return the count of integers printed
