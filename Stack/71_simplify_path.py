class Solution:
    def simplifyPath(self, path: str) -> str:
        # Use a stack to keep track of the directories.
        stack = []
        # Split the path by '/'
        directories = path.split('/')
        result = ''

        # Go through the directories
        for d in directories:
            # If we get a blank or a ., then it's a no-op. Because we do else for actual directories, we have to give these cases
            if d == '':
                continue
            elif d == '.':
                continue
            # If we get a go back, pop the top directory in the stack
            elif d == '..':
                if stack:
                    stack.pop()
            # If the directory is an actual directory, add it to the stack
            else:
                stack.append(d)
        # Print the path by iterating through the stack from bottom to top and printing the delimeter before the directory. 
        if stack:
            for directory in stack:
                result += "/" + directory
        else:
            # For edge case of an empty stack. We have to return root no matter what. 
            result = "/"
        
        return result

# T: O(N). Splitting takes O(N). Going through the directories is O(K) if we have k directories.
# Going through the stack is O(K).
# S: O(N). We keep a stack and a directories array. 