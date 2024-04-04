class Solution:
    # We know that the range for the max capacity is from the max(weights) and the sum(weights)
    # We can do a binary search on this range and check if the weight at mid can ship the packages in d days. 
    # If it can't, we try a range from mid + 1. If it can, we try to a range from mid - 1. 
    # We also need a helper function to see how many days it would take to ship a package. 
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        # Helper function to see if we can ship all packages within d days with the given weight capacity
        def canShip(capacity):
            d = 1
            cur_weight = 0
            # Go through weights and fit as many packages as we can
            for i in range(len(weights)):
                weight = weights[i]
                # If we add this package and the weight goes over capacity, increment days and reset cur_weight to this weight
                if cur_weight + weight > capacity:
                    d += 1
                    cur_weight = weight
                # Otherwise, add this weight to the current weight
                else:
                    cur_weight += weight
            # If we can ship within d days, return True. Otherwise, false. 
            return d <= days

        while left < right:
            mid = (left + right) // 2
            # If we can ship within mid days, then move left and try to lower the capacity
            if canShip(mid):
                right = mid
            # If we can't ship within d days, increase capacity
            else:
                left = mid + 1
        return left

# T: O(NlogN) - Binary search is logN and we have to go through the weights array for every possible weight, so it's O(NlogN)
# S: O(1)