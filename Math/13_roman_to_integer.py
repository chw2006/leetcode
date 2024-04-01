class Solution:
    # Create a table mapping the roman letter to its value.
    # Get the current letter's value, if it is smaller than the next index's value, it is negative.
    # So decrement the current value from total. 
    # Otherwise, add the value to the total
    def romanToInt(self, s: str) -> int:
        total = 0
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for i in range(len(s)):
            c = s[i]
            # If the next index is in bounds and the value at current index is smaller than the value at next, decrement the current value.
            if i + 1 < len(s) and map[c] < map[s[i + 1]]:
                total -= map[c]
            # Otherwise, add the current value.
            else:
                total += map[c]
        
        return total

# S: O(N) - we must traverse the entire string
# T: O(1) - we use a map, but it is a constant map with only 7 values in it. 