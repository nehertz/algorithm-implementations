"""
Times a program and prints how long it took. Import it to a program to time it.

Based on PaulMcG's (https://stackoverflow.com/users/165216/paulmcg) answer on this Stack Overflow question: https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution/12344609#12344609.
"""

import atexit
from time import time, strftime
from datetime import timedelta, date

def start():
    start_time = time()
    atexit.register(finish, start_time)

def time_print(time):
    """ Prints a formatted message with the elapsed amount of time """
    final_time = timedelta(seconds=time)
    print("="*40 + "\n\nThe process took {}.{:03} seconds to execute.".format(final_time.seconds, final_time.microseconds))

def finish(start_time):
    """ Collects the time when the program exits and calculates
    elapsed time of the program, which is passed to the print function """
    end_time = time()
    elapsed_time = end_time - start_time
    time_print(elapsed_time)