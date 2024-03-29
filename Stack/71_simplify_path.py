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
    
# Meta asks this problem with a variation. They give you 2 inputs, one for the current working directory and another for the destination path. 
def metaSimplifyPath(cwd, destination):
    # This should be the very similar to the original problem
    # One way to solve it would be to join the cwd and destination strings.
    # It depends on how they format the inputs. If they are required to have a '/' at the start of each path, then we do not need to join with a '/'.
    # Although technically it should not matter. 
    stack = []
    result = ""
    combined = cwd + destination
    directories = combined.split('/')

    # Go through each directory, if we see a blank, ignore it. If we see a ., ignore it. If we see a .., pop from stack.
    # If we see a directory, add it to stack. 
    for dir in directories:
        if dir == '' or dir == '.':
            continue
        elif dir == '..':
            stack.pop()
        # Case of a real directory
        else:
            stack.append(dir)
    
    # Print the path. Since it needs to start with a '/', add it to every directory
    if stack:
        for dir in stack:
            result += "/" + dir
    else:
        result = "/"
    
    return result

print(metaSimplifyPath("/home/foo/", "/x/y/.."))
