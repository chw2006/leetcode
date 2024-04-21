# This is a 2 pointers problem, but we are comparing 2 separate strings
# When the abbreviation is a digit, we must get its integer value. 
# If the length of the digits is longer than the remaining p1 string, return False
# Once we find its value we increment p1 by it. 
# If both characters are letters, we can compare them straight up. 
# If they do not match, we can return False

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # If both chars are alpha, then we can compare.
        # If the abbr is a number, parse the number and then increment the word pointer by that number
        # An abbr number must not start with 0. 
        # We must make sure both strings are exhausted in order to return true

        p1 = 0
        p2 = 0

        if len(abbr) > len(word):
            return False

        while p1 < len(word) and p2 < len(abbr):
            # If abbreviation is alpha, we can compare
            if abbr[p2].isalpha():
                if word[p1] != abbr[p2]:
                    return False
                p1 += 1
                p2 += 1
            # If it is a number, we must find its number and fast forward p1 by it. 
            else:
                # If abbr is a number
                num = 0
                # Look for leading 0s
                if abbr[p2] == '0':
                    return False
                while p2 < len(abbr) and abbr[p2].isdigit():
                    num = num * 10 + int(abbr[p2])
                    p2 += 1
                # Increment p1 by num
                p1 += num
                
        # Both pointers must be at the end of each word in order to return True
        if p1 == len(word) and p2 == len(abbr):
            return True
        else:
            return False

#T: O(N) we make one pass through both strings.
#S: O(1) we only keep track of pointer values. 
