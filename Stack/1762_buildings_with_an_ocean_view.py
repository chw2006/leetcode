def find_buildings(heights):
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
    
input = [2, 2, 2, 2, 2]
res = find_buildings(input)
print(res)