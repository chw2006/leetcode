class Solution:
    # Use a stack to maintain all the letters and their count
    # If the letter at the top of the stack is not the same as current, add the letter and its count to the stack.
    # If a letter at the top of the stack is the same as current, increment that letter's count
    # Whenever a letter's count gets to the value k, pop that letter from the stack.
    # Go through the stack at the end and build the string using the count from the stack.
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            # If top of stack is equal to current char, increment it.
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                # If the count is equal to k, pop it from the stack.
                if stack[-1][1] == k:
                    stack.pop()
            # Otherwise just add to the stack
            else:
                stack.append([c, 1])
        res = ""
        # Go through stack and build the string
        for item in stack:
            for i in range(item[1]):
                res += item[0]
        
        return res

# T: O(N) - We go through the string once and then the stack once, but separately. So it rounds down to O(N). 
# S: O(N) - We use a stack and a string builder for the result, so O(N). 
