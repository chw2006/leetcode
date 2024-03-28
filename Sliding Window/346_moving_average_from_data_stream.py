from collections import deque
# This problem is trickier than regular sliding window since it gives you the input as a stream. 
# To account for that, use a deque as the window. Add to the window until the window gets too large, then pop from the left. 
# The average is just the sum of the window divided by its size. 
class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.window = deque()
        self.sum = 0

    def next(self, val):
        self.window.append(val)
        self.sum += val
        if len(self.window) > self.size:
            self.sum -= self.window.popleft()
        return self.sum // len(self.window)
    
obj = MovingAverage(3)
print(obj.next(1))
print(obj.next(10))
print(obj.next(3))
print(obj.next(5))

#T: Init: O(1), next: O(N) since it will be called N times for N items. 
#S: if K is the size of the window, we use O(K)