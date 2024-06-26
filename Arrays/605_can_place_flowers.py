class Solution:
    # We can only plant flowers if the spot is 0 and 2 adjacent spots are 0.
    # There are 3 edge cases to consider, when we are at either end of the flowerbed or if the flowerbed is only size 1.
    # At the start, we can plant at i = 0 if it's 0 and i + 1 is also 0. 
    # At the end, we can plant at i = len(flowerbed) - 1 if that spot and i - 1 are 0. 
    # If both sides are out of bounds, we can also plant if i is 0. 
    # Whenever we hit any of these conditions, set a 1 at i in the flowerbed.
    # We also decrement n.
    # If at any point, n is less than or equal to 0, we return True.
    # At the end, we return False. 
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        def canPlant(i):
            # Start the left and right at 0
            left = 0
            right = 0
            # If left and right are in-bounds, set them
            if i - 1 >= 0:
                left = flowerbed[i - 1]
            if i + 1 < len(flowerbed):
                right = flowerbed[i + 1]
            # We can only plant if the flowerbed is 0 and its neighbors are 0
            if flowerbed[i] == 0 and left == 0 and right == 0:
                return True
            
            return False

        # If they are asking to plant 0 flowers, we can automatically return True. 
        if n == 0:
            return True

        # Go through the flower bed
        for i in range(len(flowerbed)):
            # See if we can plant here
            if canPlant(i):
                # If we can set that spot to 1 and decrement n
                flowerbed[i] = 1
                n -= 1
            # If n is 0 at any point, return True. 
            if n == 0:
                return True
        
        return False

# T: O(N), we traverse at most the entire flowerbed.
# S: O(1), we only keep track of pointers. 
