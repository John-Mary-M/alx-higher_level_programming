#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Prints the first x elements of a list and returns the number of elements
    printed.
    """
    count = 0  # init a variable 2 keep track of the no. of elements printed
    for i in range(x):  # Loop through the range from 0 to x-1
        try:
            print(my_list[i], end="")  # Print the element at index i
            count += 1  # Increment the count of elements printed
        except IndexError:  # If an IndexError occurs
            break  # Exit the loop
    print()  # Print a newline character after all the elements are printed
    return count  # Return the count of elements printed
