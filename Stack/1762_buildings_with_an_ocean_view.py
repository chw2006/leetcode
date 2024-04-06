from collections import deque

def find_buildings(heights):

    def stack():
        stack = []
        # Go through all heights
        for i in range(len(heights)):
            # If the stack is populated and the element at the top of the stack is smaller than the current element:
            # pop from the stack. 
            while stack and heights[stack[-1]] <= heights[i]:
                stack.pop()
            # Once we've popped all elements smaller than this element from the stack, add this element to it. 
            stack.append(i)
        
        return stack
    #T: O(N), go through heights once.
    #S: O(N), we use a stack

    def queue():
        # Use a deque to keep track of the result
        q = deque()
        max_seen = 0
        # Go from right to left and add the indices of 
        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]
            # If height is larger than the max seen so far...
            # Add it to the queue on its left (so it's in sorted order)
            if height > max_seen:
                q.appendleft(i)
                # Set max_seen to this height
                max_seen = height
        return list(q)
    
    # T: O(N) - have to go through heights once
    # S: O(N) - in the worst case, we keep all the buildings in the result'

    queue()
    
input = [2, 2, 2, 2, 2]
res = find_buildings(input)
print(res)
