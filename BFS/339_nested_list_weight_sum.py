
from collections import deque


def isList(item):
    return isinstance(item, list)

# Do BFS on the nestedList. 
# When we see a list, put its values in the back of the queue.
# For every level we are on, we only process integers. 
def depthSum(nestedList):
    q = deque(nestedList)
    depth = 1
    total = 0
    while q:
        for i in range(len(q)):
            # Get the first item in the queue
            curr = q.popleft()
            # If curr is actually a list 
            if isList(curr):
                q.extend(curr)
            # If curr is a number
            else:
                total += (depth * curr)
        depth += 1
    return total

nestedList = [[1,1],2,[1,1]]
print(depthSum(nestedList))
nestedList = [1,[4,[6]]]
print(depthSum(nestedList))
nestedList = [[1,1],2,[1,1],1,[4,[6]]]
print(depthSum(nestedList))

    