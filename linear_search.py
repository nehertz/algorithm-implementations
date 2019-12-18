"""
Just an implementation of linear search.
"""

import timing
import os

def manual_in():
    """ Perform linear search using manual entry of a list and search query """

    confirm = 'n'

    while (confirm == 'n'):
        in_str = input("> Please enter a list of numbers, characters, or strings, separated by spaces (e.g. '32 11 str str2 hello 9 2')\n")

        l = in_str.split(" ")
        confirm = '?'

        # Error checking
        while (confirm == '?'):
            confirm = input("> List: " + str(l) + ". Does this look correct? [y/n]: ")

            if (confirm == 'y'):
                search = input("\n> Search for: ")
                timing.start() # Start the timer
                linear_search(l, search) # Make the search

                return
            elif (confirm == 'n'):
                continue
            else:
                print("> ERROR: Please enter either 'y' for yes or 'n' for no.")
                confirm = '?'
                continue

    return

def file_in():
    """ Perform linear search using a list and search query read from a file """

    print("> Input file requirements:")
    print("[ Line 1: List to be searched, where each item is separated by a white space character")
    print("[ Line 2: Item to be searched for")
    print("[ End of file")

    success = 'n'

    while(success == 'n'):
        f_name = input("> Enter filename: ")

        try:
            f = open(f_name, 'r')
        except OSError:
            print("> ERROR: Could not open/read " + f_name + ".")
            continue
        
        with f:
            l = ((f.readline()).rstrip().split())
            search = f.readline()

            print("List: " + str(l))
            print("Search: " + search)

            timing.start() # Start the timer
            linear_search(l, search) # Make the search
            success = 'y'
            
    return

def linear_search(list, value):
    """ Searches for a value in a list linearly! """

    for i, val in enumerate(list):
        if (val == value):
            print(">> Found {} in the list at index {}.".format(value, i))
            return

    print(">> {} is not in the list.".format(value))
    return


def main():
    """ Entry point """

    # Begin user input
    print("> Welcome to this implementation of linear search!")

    option = '?'

    while(option == '?'): # Check for input error
        option = input("> 1. Manually enter input\n> 2. Enter input from a file\n")

        if (option == '1'):
            # Collect input from command line
            manual_in()
        elif (option == '2'):
            # Collect input from file
            file_in()
        else:
            print("> ERROR: Incorrect option.")
            option = '?'
            continue
            

if __name__ == "__main__":
    main()