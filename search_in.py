import os
import re

"""
Helper functions that collect input for searches
"""

def manual_in():
    """ Reads and returns user-entered input list and search term from command line """

    confirm = 'n'

    while (confirm == 'n'):
        # Collect input
        in_str = input("> Please enter a list of numbers, characters, or strings, separated by white space (e.g. '32 11 str str2 hello 9 2')\n")

        # Check if something was entered that can be parsed by the regex
        if ((re.search(r"([A-Za-z0-9]+\s)+", in_str) == None) or (re.search(r"[^A-Za-z0-9\s]", in_str) != None)):
            # Incorrect input was entered
            print("> Please do not use special characters.\n")
            continue
        
        # Create the list from the input
        l = re.split(r"\s+", in_str)

        for i, val in enumerate(l):
            # Convert list values to int if need be
            if (val.isnumeric()):
                l[i] = int(l[i])

        confirm = '?'

        # Error checking
        while (confirm == '?'):
            confirm = input("> List: " + str(l) + ". Does this look correct? [y/n]: ")

            if (confirm == 'y'):
                while (True):
                    search = input("\n> Search for: ")

                    if ((re.search(r"[^A-Za-z0-9]", search) != None)):
                        # Incorrect input was entered
                        print("> Please limit your search to alphanumerics.\n")
                        continue

                    if (search.isnumeric()):
                        # Convert search term to int if need be
                        search = int(search)

                    # Input checked and confirmed, return from function
                    return [l, search]
            elif (confirm == 'n'):
                # Input denied, go back to input entry
                continue
            else:
                print("> ERROR: Please enter either 'y' for yes or 'n' for no.")
                confirm = '?'
                continue

    return

def file_in():
    """ Reads and returns input list and search term from a file """

    print("> Input file requirements:")
    print("[ Line 1: List to be searched, where each item is separated by a white space character")
    print("[ Line 2: Item to be searched for")
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

            if ((re.search(r"([A-Za-z0-9]+\s)+", in_str) == None) or (re.search(r"[^A-Za-z0-9\s]", in_str) != None)):
                # Incorrect input was entered
                print("> Your file does not format its input list correctly.\n")
                continue

            l = (re.split(r"\s+", in_str))

            for i, val in enumerate(l):
                # Convert list values to int if need be
                if (val.isnumeric()):
                    l[i] = int(l[i])

            # Read search term from input with error checking
            search = f.readline()

            if ((re.search(r"[A-Za-z0-9]+", search) == None)):
                # Incorrect input was entered
                print("> Your file does not format its search term correctly.\n")
                continue

            if (search.isnumeric()):
                # Convert search term to int if need be
                search = int(search)

            # Print list and search term
            print("List: " + str(l))
            print("Search term: " + search)

            return [l, search]
    
    return