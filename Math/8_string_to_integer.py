class Solution(object):
    # Go until all white spaces are read at the start.
    # Then the next char may be a sign, assign 1 for + and -1 for minus. Increment i. Make sure to check if i is in bounds before indexing. 
    # Then we read while the current char is no longer a digit. If it is a digit, get its int representation by adding num * 10 to int(s[i])
    # If the number is larger than what a 32 bit num can hold, we need to truncate it.
    # If sign is positive, we return 2^31 - 1. If it's negative, return 2^31. 
    # Return sign * num. 
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        sign = 1
        i = 0
        num = 0
        # Skip all whitespaces at front
        while i < len(s) and s[i] == ' ':
            i += 1

        # Next char could be a sign, assign accordingly
        if i < len(s):
            if s[i] == '+':
                sign = 1
                i += 1
            elif s[i] == '-':
                sign = -1
                i += 1
        
        # Next chars must be digits, read all
        while i < len(s) and s[i].isdigit():
            num = num * 10 + int(s[i])
            i += 1

        # Must truncate if it's larger than 2^31, but it is based on sign
        if num >= 2 ** 31:
            if sign == 1:
                num = 2 ** 31 - 1
            else:
                num = 2 ** 31
        
        return num * sign

# T: O(N)
# S: O(1)