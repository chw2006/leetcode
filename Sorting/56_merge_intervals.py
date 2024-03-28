class Solution:
    # Sort the intervals first
    # Go through the intervals and compare current one to the previous. 
    # If the end of the last is larger than the start of the current, then we have an overlap. Update the result with a new end that is max(curr, last)
    # Otherwise, there is no overlap. Just copy to the result. 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort this interval by the first value in the interval
        intervals.sort()
        # Insert the first interval in here for edge case of it only having 1 interval. 
        res = [intervals[0]]
        print(intervals)
        for i in range(1, len(intervals)):
            # Get the previous value we put into res
            last = res[-1]
            curr = intervals[i]
            # If the last's end is larger than the current's start, there is overlap
            if last[1] >= curr[0]:
                # Because we know there's overlap, modify the last item to end at max(curr, last)
                res[-1][1] = max(curr[1], last[1])
            # No overlap
            else:
                # Append curr
                res.append(curr)
        
        return res