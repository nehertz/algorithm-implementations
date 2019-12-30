"""
Just an implementation of insertion sort
"""

import timing
import sort_in

def pretty_list(l, sorted_i):
    """ Returns a insertion sort list as a string with a pipe to separate the sorted sublist from the unsorted sublist """

    length = len(l)

    if (sorted_i == length):
        # The list is sorted, return a simple stringified form of the list
        return str(l)

    pretty = "["

    i = 0

    while (i < sorted_i):
        pretty += (str(l[i]) + ", ")
        i += 1

    pretty += "| "

    while (i < length - 1):
        pretty += (str(l[i]) + ", ")
        i += 1

    pretty += (str(l[length - 1]) + "]")

    return pretty

def swap(l, i, j):
    """ Swaps two values in a list """
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def sort(l):
    # Set i to 1, since the first element is already sorted in its own sublist of size one
    i = 1
    passes = 0

    print("> (" + str(passes) + ")\t" + pretty_list(l, i))

    while (i < len(l)):
        passes += 1
        j = i

        while (j > 0 and l[j - 1] > l[j]):
            # Compare the current value with the elements in the sorted list to find its place
            swap(l, j, j - 1)
            j -= 1

        i += 1

        print("> (" + str(passes) + ")\t" + pretty_list(l, i))

        if (i == len(l)):
            # The index is the last index of the list, meaning the entire list is sorted
            return

def main():
    # Begin user input
    print("> Welcome to this implementation of insertion sort!")

    option = '?'

    while(option == '?'): # Check for input error
        option = input("> 1. Manually enter input\n> 2. Enter input from a file\n")

        if (option == '1'):
            # Collect input from command line
            l = sort_in.manual_in()

            # Start timer and conduct search
            timing.start()
            sort(l)

            return
        elif (option == '2'):
            # Collect input from file
            l = sort_in.file_in()

            # Start timer and conduct search
            timing.start()
            sort(l)

            return
        else:
            print("> ERROR: Incorrect option.")
            option = '?'
            continue

    return

if __name__ == '__main__':
    main()