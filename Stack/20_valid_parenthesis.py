# Rationale: Add all opening chars onto the stack. When encountering a closing char...
# Check that the top of the stack is its counterpart. 
# If it's not, we know the string is not valid.
# If it does match, pop the top value from the stack. 
# The resulting stack of a valid string should have no length. Otherwise, return false.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        # Go through every character in the string
        if (len(s) > 1):
            for c in s:
                # Check if the current char has a matching char in the stack
                if c == '(' or c == '[' or c == '{':
                    stack.append(c)
                # If a closing character does not have a corresponding opening character at the top of the stack, return false
                # If it is the corresponding closing character, pop the value from the stack
                elif c == ')':
                    if len(stack) == 0 or stack[-1] != '(':
                        return False
                    stack.pop()
                elif c == ']':
                    if len(stack) == 0 or stack[-1] != '[':
                        return False
                    stack.pop()
                elif c == '}':
                    if len(stack) == 0 or stack[-1] != '{':
                        return False
                    stack.pop()
            # If all the parenthesis are properly closed, the length of the stack will be 0
            if len(stack) > 0:
                return False
            else:
                return True
        else:
            return False

# T: O(N) - have to go through entire stack
# S: O(N) - Need to keep track of the openings in a stack. 