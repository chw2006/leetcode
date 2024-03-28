class NumArray:
    # Create a prefix sum in the constructor.
    # For sumRange, we get the range by taking the value at the right and subtracting the value before left.
    # If left is 0, then we only take the prefix value at right. 
    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)
    # T: O(N)
    # S: O(N)

    def sumRange(self, left: int, right: int) -> int:
        # If left is 0, we only care for the prefix sum at right since the sum at 0 is 0. 
        if left == 0:
            return self.prefix[right]
        # Otherwise, we take the sum at right and subtract the one previous to left. 
        else:
            return self.prefix[right] - self.prefix[left - 1]
        

    # T: O(1)
    # S: O(1)
    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)