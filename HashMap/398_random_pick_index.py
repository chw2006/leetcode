import random
class Solution:
    def __init__(self, nums: List[int]):
        self.map = {}
        self.nums = nums
        # Use a table to store the indices as a list for each number seen
        for i in range(len(nums)):
            num = nums[i]
            if num in self.map:
                self.map[num].append(i)
            else:
                self.map[num] = [i]

    # Use reservoir sampling for this since we want space to be O(1). This is the preferred solution. 
    # Since we cannot keep the indicies for each number we meet, we instead use the count. 
    # For the count, we know that whatever the count is, the probability of picking a random index is 1/count. 
    # So we pick a random number between 1 and the count and if that number is the same as the count, we set pick to that index. 
    def reservoir_sampling(self, target):
        count = 0
        pick_index = 0
        # Look for target in the array. 
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                # If we find the target in the array, increment the count
                count += 1
                # Pick a random number between 1 and count.
                # If it is equal to count, we set the pick_index to the current index
                if random.randint(1, count) == count:
                    pick_index = i
        return pick_index
    
    # This is the O(N) space solution, but this is actually faster because we only go over the array once in the constructor. 
    # The rest is all done via table look up which is constant time.
    # Once we know the indicies of target, we randomly choose one. 
    def hash_table(self, target):
        picks = self.map[target]
        return random.choice(picks)
    
    # This is not quite constant space, but also not O(N) space and it passes LC. But it is slower. 
    # For every time we see target, add its indicies to a list. Then randomly choose from that list. 
    # This is definitely worse than the hash table method for speed, but might save on space. 
    def list_choice(self, target):
        picks = []
        # Look for target in the array. 
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                picks.append(i)
                
        return random.choice(picks)
    
    def pick(self, target: int) -> int:
        return self.hash_table(target)