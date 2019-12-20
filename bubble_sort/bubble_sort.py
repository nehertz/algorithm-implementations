"""
Just an implementation of bubble sort
"""

import timing

def swap(l, i, j):
    """ Swaps two values in a list """
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

def sort(l):
    passes = 0
    print("> Inital list:\t" + str(l))

    while (True):
        swaps = 0
        passes += 1

        if (passes == len(l) - 1):
            # Optimization: the n-th pass puts the final item in its place, so there's no need to check the last n - 1 items
            print("> (n - 1)th pass reached; swapping first and second elements, completing the sort")
            swap(l, 0, 1)
            print("> Sorted list:\t" + str(l))
            return

        for i, val in enumerate(l):
            # For each item in the list, compare it with its adjacent item and swap the two if it is greater
            if (i < len(l) - 1):
                if (val > l[i + 1]):
                    swap(l, i, i + 1)
                    swaps += 1
        
        if (swaps == 0):
            # Optimization: No swaps were made during this pass, so the list is sorted
            print("> No swaps were made during this pass. The list is sorted.")
            return

        print("> Pass " + str(passes) + ":\t" + str(l))

    return

def main():
    l = [3, 5, 8, 4, 1, 9, -2]
    l2 = [1, 2, 3, 4, 5, 6, 7, 8]
    l3 = [1, 2, 3, 4, 5, 6, 8, 7]

    sort(l)

if __name__ == '__main__':
    main()