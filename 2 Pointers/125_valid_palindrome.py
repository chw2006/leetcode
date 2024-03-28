class Solution:
    # This is a classic 2 pointers problem
    # This problem requires that we only take in alphanumeric characters (isalnum())
    # If both left and right are alphanumeric, they must equal.
    # Otherwise, we return False.
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            # If they are both alphanumeric, we can compare
            if s[left].isalnum() and s[right].isalnum():
                # If they aren't equal, return False
                if s[left].lower() != s[right].lower():
                    return False
                #Otherwise, increment left, decrement right
                left += 1
                right -=1
            # If both or either are not alphanumeric, move both pointers until they are
            else:
                while left < len(s) and not s[left].isalnum():
                    left += 1
                while right > 0 and not s[right].isalnum():
                    right -= 1
        
        return True
    
# T: O(N) - we have to go through the whole string
# S: O(1)
