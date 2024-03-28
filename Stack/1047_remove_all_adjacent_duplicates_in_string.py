class Solution:
    # Use a stack to keep track of letters we've encountered so far. 
    # If the top element of the stack is the same as the current letter, pop from stack
    # Otherwise, add it to the stack
    # In this case we only have to make one pass. 
    # Join the stack into a string as the result
    def removeDuplicates(self, s: str) -> str:
        stack = []
        i = 0
        for c in s:
            if stack:
                # Check the top of the stack
                top = stack[-1]
                if c != top:
                    # Add to stack
                    stack.append(c)
                else:
                    # Pop from the stack
                    stack.pop()
            else:
                # Append the character to the stack
                stack.append(c)
        
        return "".join(stack)

# T: O(N) have to make one pass through the string
# S: O(N) as we have to store every value on the stack at some point. 