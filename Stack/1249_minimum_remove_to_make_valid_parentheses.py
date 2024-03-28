class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        # Turn the string into an array
        array = list(s)
        for i in range(len(array)):
            # If we get a beginning parenthesis, add it to the stack
            if s[i] == "(":
                stack.append(i)
            # If we get an ending parenthesis, make sure it has a matching beginning
            elif s[i] == ")":
                # Pop from the stack to match this parenthesis
                if stack:
                    stack.pop()
                # If the stack is empty, then remove the closing parenthesis
                else:
                    array[i] = ''
        # If the stack is not empty by the end of the string, that means there were unclosed parenthesis. Remove the opening parens from the string. 
        while stack:
            array[stack.pop()] = ''

        result = "".join(array)
        return result

# T: O(N), we go through every char in the string.
# S: O(N), we use a stack and copy the string into a string builder. Also, join at the end is O(N)

