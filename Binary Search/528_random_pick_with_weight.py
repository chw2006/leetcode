import random

class pick:
    # We need to use a combination of prefix sums and binary search
    # In the constructor, calculate the prefix sums and get the total.
    # In pickIndex, randomly generate a number between 0 and total, this is the target.
    # Do binary search: find the mid. If the mid is smaller than the target, go right.
    # If the mid is larger or equal to the target, go left (set r to mid)
    # Answer is in the left pointer. 
    def __init__(self, w):
        # Calculate the prefix sum and total
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)
        self.total = total

    def pickIndex(self):
        # Pick a number beween 0 and total
        target = random.uniform(0, self.total)
        # Use binary search to find the range this target belongs in
        l = 0
        r = len(self.prefix_sum)

        while l < r:
            # Find the mid
            mid = (l + r) // 2
            # If mid is smaller than target, go right
            if self.prefix_sum[mid] < target:
                l = mid + 1
            # Otherwise go left
            else:
                r = mid
        
        return l

w = [1, 3, 2]
p = pick(w)
print(p.pickIndex())
    
# T: O(N) to generate the prefix sums. O(logN) for pickIndex. 
# S: O(N) for constructor, O(1) for pickIndex()
    
