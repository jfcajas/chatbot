"""
    This class notifies the user if live support is available or not
    If live support is available, it notifies the user that they have been
    added to the queue

"""

import datetime

dt = datetime.datetime.now()
day = dt.weekday()

start = datetime.time(8, 0, 0)
end = datetime.time(20, 0, 0)


def time_in_range(start, end, current):
    if dt.weekday() == 5 or dt.weekday() == 6 or not (start >= current.time() <= end):
        return True


def final(match):
    if time_in_range(start, end, dt):
        print('Sorry, agents are only available Monday through Friday 8am to 8pm')
    else:
        print('Agent available! Adding you to queue for live support...')
        # TODO Future Feature: add handler to notify live agent of customer in queue




