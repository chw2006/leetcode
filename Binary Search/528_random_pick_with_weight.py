import random

class pick:
    # We need to use a combination of prefix sums and binary search
    # In the constructor, calculate the prefix sums and get the total.
    # In pickIndex, randomly generate a number between 0 and total, this is the target.
    # Do binary search: find the mid. If the mid is smaller than the target, go right.
    # If the mid is larger or equal to the target, go left
    # Answer is in the left pointer. 
    # Follow-up question: what if the array is just one number and we call pick index a million times, leading to random being called a million times?
    # We can have a base case where if the length of the array is 1, we return 0. 
    def __init__(self, w):
        # Calculate the prefix sum and total
        self.prefix_sum = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sum.append(total)
        self.total = total

    def pickIndex(self):
        # For the case where there is only 1 value in the array. 
        if len(self.prefix_sum) == 1:
            return 0
        # Pick a number beween 0 and total
        target = random.uniform(0, self.total)
        # Use binary search to find the range this target belongs in
        l = 0
        r = len(self.prefix_sum) - 1
        # We want to pick the first index that has a larger value than target. 
        while l <= r:
            # Find the mid
            mid = (l + r) // 2
            # If mid is smaller than target, go right
            if self.prefix_sum[mid] < target:
                l = mid + 1
            # Otherwise go left
            else:
                r = mid - 1
        # We want the first index larger than the target.
        return l

w = [1, 3, 2]
p = pick(w)
print(p.pickIndex())
    
# T: O(N) to generate the prefix sums. O(logN) for pickIndex. 
# S: O(N) for constructor, O(1) for pickIndex()
    
