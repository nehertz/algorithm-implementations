"""
Just an implementation of selection sort
"""

import timing

def pretty_list(l, sorted_i):
    pretty = "["

    i = 0

    while (i < sorted_i):
        pretty += (str(l[i]) + ", ")
        i += 1

    pretty += "| "

    while (i < len(l) - 1):
        pretty += (str(l[i]) + ", ")
        i += 1

    pretty += (str(l[len(l) - 1]) + "]")

    return pretty

def swap(l, i, j):
    """ Swaps two values in a list """
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def sort(l):
    passes = 0
    print("> Inital list:\t" + pretty_list(l, 0))

    sorted_i = 0

    while (True):
        passes += 1
        # Set i to make it so we only loop over the unsorted sublist
        i = sorted_i
        # Reset index of smallest number
        small_i = sorted_i

        while (i < len(l)):
            if (l[i] < l[small_i]):
                # New smallest number located
                small_i = i
            
            i += 1

        # Place the smallest unsorted item at the end of the sorted sublist and increment sorted index
        swap(l, sorted_i, small_i)
        sorted_i += 1

        if (sorted_i == len(l) - 1):
            # The sorted index is the last index of the list, meaning the entire list is sorted
            print("> Sorted list:\t" + pretty_list(l, sorted_i))
            return

        print("> Pass " + str(passes) + ":\t" + pretty_list(l, sorted_i))



def main():
    l = [3, 5, 8, 4, 1, 9, -2]
    l2 = [1, 2, 3, 4, 5, 6, 7, 8]
    l3 = [1, 2, 3, 4, 5, 6, 8, 7]

    timing.start()
    sort(l3)

if __name__ == '__main__':
    main()