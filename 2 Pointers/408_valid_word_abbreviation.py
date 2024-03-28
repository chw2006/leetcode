# This is a 2 pointers problem, but we are comparing 2 separate strings
# When the abbreviation is a digit, we must get its integer value. 
# If the length of the digits is longer than the remaining p1 string, return False
# Once we find its value we increment p1 by it. 
# If both characters are letters, we can compare them straight up. 
# If they do not match, we can return False

def valid_word_abbreviation(s, abbr):
    p1 = 0
    p2 = 0
    while p1 < len(s) and p2 < len(abbr):
        # Case for when abbr is a digit
        if abbr[p2].isdigit():
            digit = 0
            # The digit can be multiple characters, turn that into an integer
            while p2 < len(abbr) and abbr[p2].isdigit():
                # If we have a digit that is multipe characters, calculate its value
                # by using prev * 10 + digit
                digit = (digit * 10) + int(abbr[p2])
                # Increment p2
                p2 += 1
                if digit > len(s) - p1:
                    return False
            # Increment p1 depending on the value of the digit
            p1 += digit
        else:
            # For the case where both characters are letters
            # If they aren't equal, we can return False
            if s[p1] != abbr[p2]:
                return False
            # Increment both pointers
            p1 += 1
            p2 += 1
    # If we get here, we can return True
    return True

s = 'internationalization'
abbr = 'i18n'
print(valid_word_abbreviation(s, abbr))  # True
s = 'apple'
abbr = 'a2e'
print(valid_word_abbreviation(s, abbr))  # False'

#T: O(N) we make one pass through both strings.
#S: O(1) we only keep track of pointer values. 