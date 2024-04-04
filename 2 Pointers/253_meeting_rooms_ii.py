"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    # Take the start times and end times and separate them into their own arrays
    # Sort them both
    # Go through both arrays with their own pointers.
    # If the end time > start time, increment rooms and move the start pointers
    # Otherwise, decrement rooms and increment the end times. 
    # Set res to the max of rooms and return it
    def min_meeting_rooms(self, intervals) -> int:
        i = 0
        j = 0
        rooms = 0
        res = 0
        # Separate the start and end into 2 arrays and sort them
        start = []
        end = []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        start = sorted(start)
        end = sorted(end)

        # Only loop until we exhaust the starting array (end will just decrement rooms)
        while i < len(start):
            # If the end is larger than the start, we need to use another room. Also increment i to get next start time
            if end[j] > start[i]:
                i += 1
                rooms += 1
            # Otherwise, we decrement rooms and increment j for next end time. 
            else:
                j += 1
                rooms -= 1
            res = max(res, rooms)
        
        return res
# T: O(NlogN) - Sorting takes NlogN. Compared to the iteration, that is far larger. 
# S: O(N) - We keep the start and end arrays
    
# Meta has a similar problem to this asking which value is within the most intervals. It's basically the same problem. 
# You are given n bounded integer intervals [[start1, end1], [start2, end2]; determine any point that belongs to the maximum number of intervals.
# This is basically the same problem. Once you visualize it it'll become much more clear.
# With the rooms problem, if you plot the meetings on a graph you can see how many rooms you need given the meetings going on concurrently.
# It's the same with the number that belongs to the max # of intervals, because that number would cross the most amount of intervals (it's the # of meeting rooms)
# So we solve it with the same solution. We sort the start and end times.
# If any end time is larger than the start time, we increase the frequency and note the start time. We do this because we know that the start time is part of the interval that includes the end time.
# We have to sort the arrays because for any end time, any start time that is before it has to have an interval that it intersects with. 
# We keep track of the max interval and the start val for that max interval. That is our result.
def findMaxIntervals(intervals):
    # Intervals are tuples, so put them in 2 sorted lists.
    start = []
    end = []
    for s, e in intervals:
        start.append(s)
        end.append(e)
    start = sorted(start)
    end = sorted(end)
    s = 0
    e = 0
    max_freq = 0
    max_num = 0
    cur_freq = 0

    # We only care for what's in start
    while s < len(start):
        # If end is larger or equal to start
        if end[e] >= start[s]:
            cur_freq += 1
            # If cur_freq is larger than max, set max to it
            # Also set the max num
            if cur_freq > max_freq:
                max_freq = cur_freq
                max_num = start[s]
            s += 1
        else:
            # If start is larger than end
            e += 1
            # Decrement frequecy
            cur_freq -= 1
    
    return (max_freq, max_num)

intervals = [[1, 5], [2, 4], [3, 13], [6, 10], [10, 12], [11, 13]]
print(findMaxIntervals(intervals)) # 3, 3