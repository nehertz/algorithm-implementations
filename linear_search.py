"""
Just an implementation of linear search.
"""

import timing
import search_in

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
            l, search = search_in.manual_in()

            # Start timer and conduct search
            timing.start()
            linear_search(l, search)

            return
        elif (option == '2'):
            # Collect input from file
            l, search = search_in.file_in()

            # Start timer and conduct search
            timing.start()
            linear_search(l, search)

            return
        else:
            print("> ERROR: Incorrect option.")
            option = '?'
            continue
            

if __name__ == "__main__":
    main()