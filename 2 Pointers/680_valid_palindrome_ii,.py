class Solution:
    # Try to find a palindrome using 2 pointers, but when you meet a string that does not match, do not return false. 
    # We are allowed to delete at least one character. However, we cannot predict which one to to delete that will result in a valid palindrome
    # To alleviate that, we see if the rest of the string is a palindrome by either decrementing L or incrementing R. 
    # If either one results in a valid palindrome, we return True. 
    def validPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1

        # Helper function to decide if the substring is a palindrome
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        # Use 2 pointers to determine if it's a valid palindrome
        while L < R:
            # When they do not equal, call is_palindrome() on the substrings of either incremeing L or decrementing R
            if s[L] != s[R]:
                return is_palindrome(L, R-1) or is_palindrome(L+1, R)
            else:
                # If they are equal, just increment L and R
                L += 1
                R -= 1
        
        return True

# T: O(N) - We have to go through the entire string in the worst case.
# S: O(1) - We only keep pointers. 
