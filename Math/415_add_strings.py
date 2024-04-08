class Solution:
    # Need to treat this like you're doing a math problem by hand.
    # Go from the end of each number string and add them. 
    # The current sum is always the sum of the 2 values and the carry.
    # We insert it into the string as that value mod 10. 
    # Then we calculate the carry by dividing that value by 10. 
    # At the end, if there is still a carry, append it to the result.
    # Reverse the string since the values added to the result are backwards. 
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = []
        cur_i = 0
        cur_j = 0

        # Go from the end to start
        while i >= 0 or j >= 0:
            # If one string is exhausted, treat it as a 0
            if j >= 0:
                cur_j = int(num2[j])
            else:
                cur_j = 0
            if i >= 0:
                cur_i = int(num1[i])
            else:
                cur_i = 0
            # Current val is the sum of both numbers and the carry
            cur_val = cur_i + cur_j + carry
            # Add sum % 10 to the string
            res.append(str(cur_val % 10))
            # New carry is sum // 10
            carry = cur_val // 10
            # Decrement pointers
            i -= 1
            j -= 1
        # If there is a carry remaining at the end, add that to the string
        if carry:
            res.append(str(carry))
        
        # We must return the result in reverse since we added it back to front. 
        return ''.join(reversed(res))

# T: O(N) - have to iterate through both strings. The join at the end is also O(N). 
# S: O(N) - we have to keep a string builder to hold the result
