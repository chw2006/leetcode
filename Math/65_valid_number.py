class Solution:
    # Valid number scenarios
    # 1. Decimal number or integer (must contain at least 1 digit)
    # 2. If it is alphabetic, it must be e or E. e or E must be followed by valid digits. (exception is a + or - at the start right after e)
    # 3. If it is a sign, + or - must be at the start. 
    # 4. If there is a decimal, there can only be one and it must be after a number is seen. 

    def isNumber(self, s: str) -> bool:

        def is_substring_valid(substring):
            # Make sure the string has a length
            if len(substring) == 0:
                return False
            digitSeen = False
            i = 0
            # The initial string after e can contain a + or -.
            if substring[i] == '+' or substring[i] == '-':
                i += 1
            # Go through the string and make sure all values are digits
            while i < len(substring):
                c = substring[i]
                if not c.isdigit():
                    return False
                # If we see at least one digit, set digitSeen to true
                else:
                    digitSeen = True
                i += 1

            return digitSeen
        
        digitSeen = False
        decimalSeen = False
        i = 0

        # + or - can only be at the start of the string
        if s[i] == '+' or s[i] == '-':
            i += 1

        # Go through the string character by character
        while i < len(s):
            c = s[i]
            # If c is alphabetic, 
            if c.isalpha():
                # If it is equal to e or E, then we must have digits before and after it. 
                if c == 'e' or c == 'E':
                    # If we have not encountered a digit before this, we can return false
                    if not digitSeen:
                        return False
                    # If we have already seen a digit, e must be followed by only digits (and a + or - at the start right after)
                    else:
                        return is_substring_valid(s[i+1:])
                else:
                    # If it is any other letter, we can return false
                    return False
            elif c == '.':
                # You can only have one decimal
                if decimalSeen:
                    return False
                else:
                    decimalSeen = True
            # We can't have + or - after the initial index
            elif c == '+' or c == '-':
                return False
            else:
                # Only other case is if it's a digit
                digitSeen = True
            i += 1
        
        # If we haven't returned false yet, we can return true if we've seen a digit
        return digitSeen