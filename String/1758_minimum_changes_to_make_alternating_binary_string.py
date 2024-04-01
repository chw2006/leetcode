class Solution:
    # Go through the array starting from 1 to len(s) - 1
    # Check if the previous value is the same as the current
    # If it is, then we have to increment changes and invert the value in the array using ^ 1. 
    def minOperations(self, s):
        def getNumOperations(s, first_value):
            changes = 0
            if first_value != s[0]:
                changes += 1
            prev_val = first_value
            for i in range(1, len(s)):
                if s[i] == prev_val:
                    changes += 1
                    prev_val = str(int(s[i]) ^ 1)
                else:
                    prev_val = s[i]
            return changes
        
        # Find the minimum number of operations between either starting with a 1 or a 0. 
        zero = getNumOperations(s, '0')
        one = getNumOperations(s, '1')

        return min(one, zero)

# There is a variant of this question from Meta that is much more difficult.
# Mr. Hamo is given a string consisting of N characters which are either 0 to 1 or vice versa. 
# He wants to make the string K-switching. In each step Mr. Hamo is allowed to switch one character from 0 to 1 or vice versa.
# It is given that a string is called K-switching if it follows the rules given below:
# There is an integer K such that K is a divisor of N.
# The first K characters of the string are 0. next K characters are 1, next-to-next K characters are 0 and so on.
# Your task is to find the minimum number of steps in which Mr. Hamo can make the given string K-switching.
# Input Format:
# The first line contains an integer, N, denoting the length of string.
# The next line Contains a string, S, denoting the string.
    
def getMinOperationsKSwitching(s):
    n = len(s)
    def getOperations(s, k):
        changes = 0
        # Pattern is starts at 0 -> 1 -> 0, etc
        curr_val = 0
        # Go through the array k times, summing up every k values in the array
        for i in range(0, len(s), k):
            total = 0
            # Sum up the values from i to i + k. 
            for j in range(i, i + k):
                total += int(s[j])
            # The amount of changes we need to make is the presumed sum of curr_val * k - total.
            changes += abs((curr_val * k) - total)
            # Switch up curr_val to the inverse for next iteration
            curr_val = curr_val ^ 1
        return changes

    min_operations = float('inf')
    # We only want to try divisors of n
    for k in range(1, n + 1):
        # Only try k values that are divisors of n
        if n % k == 0:
            min_operations = min(min_operations, getOperations(s, k))
    return min_operations

# T: O(K * N) - If K is the # of divisors for N, then the runtime is O(K * N). We iterate through s for every divisor of N. 
# S: O(1) - We only keep counters. 

s = "0011101"
print(getMinOperationsKSwitching(s)) # 4
s = "01000"
print(getMinOperationsKSwitching(s)) # 1
s = "1000111101010111"
print(getMinOperationsKSwitching(s)) # 4
