class Solution:
    # There is a dumber way to do this that is O(N^2) but this is O(N)
    # Go from right to left and figure out what is the max value seen and its index at each index
    # Then go from left to right on the string and swap the values if the max seen at that index is larger than the current
    # After swapping just once, convert the array into an int 
    def maximumSwap(self, num: int) -> int:
        map = {}
        # Turn the int into a list of num chars
        num_list = list(str(num))

        # Get the current value, the max num, and the index of the max and put it into num_list
        mn = -1
        ms = len(num_list)
        i = len(num_list) - 1

        # Go from right to left for this part
        while i >= 0:
            cur = int(num_list[i])
            num_list[i] = (cur, mn, ms)
            # If the current is larger than the max seen, set max to current and max index to i
            if cur > mn:
                mn = cur
                ms = i
            i -= 1

        # Go through the string from front to back now
        for j in range(len(num_list)):
            # If the num string char is smaller than the max seen, swap them
            cur, curMax, curIndex = num_list[j]
            if cur < curMax:
                num_list[j], num_list[curIndex] = num_list[curIndex], num_list[j]
                break
        
        # We only care about the current values, the rest don't matter.
        # Add them together to get an int
        num = 0
        for curNum, _, _ in num_list:
            num = (num * 10) + curNum
        
        # No swap occured, just return num
        return num