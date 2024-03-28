class Solution:
    # We need a stack to keep track of the previous result and the previous sign.
    # When we see a number, we want to iterate until it is no longer a number, get its int value, and save it as the curr_total.
    # When we see a sign, we can process the curr_total and add it to our result (with its sign). Then we update the sign and reset curr_total.
    # When we see an opening, add the current result and the last seen sign to the stack.
    # When we see a closing, add the current total to the result (with sign). Then pop from the stack to get the previous sign. Then add the previous result. 
    # To account for the edge case of no sign or parentheses at the end of a string, we have to add the current number to res when we return the result.  
    def calculate(self, s: str) -> int:
        res = 0
        curr_total = 0
        stack = []
        sign = 1
        i = 0
        while i < len(s):
            c = s[i]
            if c == '(':
                # When we see an opening we want to store the sign and the total before this
                stack.append(res)
                stack.append(sign)
                # Reset curr_total and sign
                sign = 1
                res = 0
            elif c == ')':
                # If we see a closing parentheses, we want to add the curr_total to res and the previous values in the stack.
                if stack:
                    # Add the current total to res
                    res += curr_total * sign
                    # Then add the previous value and its sign
                    # Previous sign
                    res *= stack.pop()
                    # Previous value
                    res += stack.pop()
                    # Reset
                    curr_total = 0
            # If c is a digit, we have to get the whole digit as a int.
            elif c.isdigit():
                # Start j at i
                j = i
                num = 0
                # Go until we no longer see a digit
                while j < len(s) and s[j].isdigit():
                    # Calculate num's value as an integer
                    num = (num * 10) + int(s[j])
                    j += 1
                # We have to backtrack j by 1 since we have to increment i later. 
                i = j - 1
                # If previous sign was +, add num to result
                curr_total = num
            # If c is a + or -, set it equal to the sign
            elif c == '+' or c == '-':
                # Add previous value to res
                res += sign * curr_total
                if c == '+':
                    sign = 1
                else:
                    sign = -1
                curr_total = 0
            # Go to the next char
            i += 1
        return res + (curr_total * sign)

# T: O(N), we go through each value in the string.
# S: O(N), we keep a stack of our values and the previous sign. 