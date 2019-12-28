import os
import re

"""
Helper functions that collect input for sorts
"""

def manual_in():
    """ Reads and returns user-entered input list from command line """

    confirm = 'n'

    while (confirm == 'n'):
        # Collect input
        in_str = input("> Please enter a list of numbers, separated by white space (e.g. '32 11 99 7 9 2')\n")

        # Check if something was entered that can be parsed by the regex
        if ((re.search(r"([0-9]+\s)+", in_str) == None) or (re.search(r"[^0-9\s]", in_str) != None)):
            # Incorrect input was entered
            print("> Please enter only integers.\n")
            continue
        
        # Create the list from the input
        l = re.split(r"\s+", in_str)

        for i, val in enumerate(l):
            l[i] = int(l[i])

        confirm = '?'

        # Error checking
        while (confirm == '?'):
            confirm = input("> List: " + str(l) + ". Does this look correct? [y/n]: ")

            if (confirm == 'y'):
                # Input confirmed, convert to int and return from function
                

                return l
            elif (confirm == 'n'):
                # Input denied, go back to input entry
                continue
            else:
                print("> ERROR: Please enter either 'y' for yes or 'n' for no.")
                confirm = '?'
                continue

    return

def file_in():
    """ Reads and returns input list from a file """

    print("> Input file requirements:")
    print("[ Line 1: List to be sorted, where each item is separated by a white space character")
    print("[ End of file")

    success = 'n'

    while(success == 'n'):
        # Collect file name input
        f_name = input("> Enter filename: ")

        # Open file with error checking
        try:
            f = open(f_name, 'r')
        except OSError:
            print("> ERROR: Could not open/read " + f_name + ".")
            continue
        
        with f:
            # Read input list from file with error checking
            in_str = f.readline().rstrip()

            if ((re.search(r"([0-9]+\s)+", in_str) == None) or (re.search(r"[^0-9\s]", in_str) != None)):
                # Incorrect input was entered
                print("> Your file does not format its input list correctly.\n")
                continue

            l = (re.split(r"\s+", in_str))

            for i, val in enumerate(l):
                l[i] = int(l[i])

            # Print list
            print("List: " + str(l))

            return l
    
    return