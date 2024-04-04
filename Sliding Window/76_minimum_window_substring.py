import collections

class Solution:
    # Use a hash map to map each char in t to its occurences (t map)
    # Use a separate hash map to map the chars to occurences in the current window (window map)
    # Keep track of the min_length, min_start, and min_end, which are the pointers to the start and end of the current min window.
    # Also keep track of the required chars needed, which is the number of unique chars in t. Keep track of current matches.
    # Use a left and right pointer to designate the start and end of the window (both 0 initially)
    # Use a for loop to go through each char in s.
    # Add the current char to the winddw
    # If the current char is in t and has the same count as it does in the window, increment matches.
    # If we have the required number of matches, then we can try to shrink the window, but first set the current result if it is the minimum we've found so far. 
    # Shrink the window by removing the char at left from the window. If the char is in t and we no longer have enough in the window, decrement matches.
    # Increment left to shrink the window
    # Using the min_start and min_end pointers, slice the string and return it, but only if we've found a min length (not infinity).
    def minWindow(self, s: str, t: str) -> str:
        t_map = collections.Counter(t)
        window_map = collections.defaultdict(int)
        left = 0
        matches = 0
        required_matches = len(t_map)
        min_length = float('inf')
        min_start = 0
        min_end = 0

        # Loop through s
        for right in range(len(s)):
            char = s[right]
            # Add char to the window
            window_map[char] += 1
            # Increment matches if this char is in t and we have the same occurences of it as in the window
            if char in t_map and window_map[char] == t_map[char]:
                matches += 1
            # Try to shrink the window if we have the required matches
            while left <= right and matches == required_matches:
                remove_char = s[left]
                # Save the current result before we try to shrink it.
                cur_length = right - left + 1
                # Only save it if it's smaller than the previous min
                if cur_length < min_length:
                    min_length = cur_length
                    min_start = left
                    min_end = right
                # Remove this from the window
                window_map[remove_char] -= 1
                # Decrement matches if the removed char is in t and we no longer have enough of it in the window
                if remove_char in t_map and window_map[remove_char] < t_map[remove_char]:
                    matches -= 1
                # Move left to shrink the window
                left += 1
        
        # If we found a window, return it. Otherwise, return an empty string
        if min_length != float('inf'):
            return s[min_start:min_end + 1]
        else:
            return ''

# T: O(N + M) - we go through every character in t to build the t map. Then we go through each char in s when processing. 
# S: O(N + M) - maps could store all chars from both strings in the worst case. 