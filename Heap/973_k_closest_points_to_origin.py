class Solution:
    # Go through the points and calculate the distance between it and (0, 0). 
    # Push a tuple into a list containing the distance and the index of the point. 
    # Heapify the list into a minheap. 
    # Pop from the minheap k times and get the points from each tuple. Add that to the result.
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        res = []
        # Calculate the distances and add it to the distances list
        for i in range(len(points)):
            p = points[i]
            # Calculate the euclidean distance
            x = p[0]**2 
            y = p[1]**2
            distance = sqrt(x + y)
            # Add the distance followed by the index
            distances.append((distance, i))
        # Heapify distances to sort by the first value in the tuple.
        heapq.heapify(distances)

        for j in range(k):
            # We only care about the index from the heap
            pi = heapq.heappop(distances)[1]
            # Add the point to the result
            res.append(points[pi])

        return res

# Time Complexity: O(K * logN)
# Space Complexity: O(N). We store all items in a heap and then k items in the result. Worst case O(N)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # This uses quick select
        # Basically, we want to find a partition index such that its k values to the left all have a smaller distance. 
        # So partition the array where all values smaller than pivot are to the left of it. Return partition index.
        # If partition index == k - 1, we have found the cut-off. Otherwise move left and right.
        # Loop from 0 to partition_index + 1 and add the original points to the result. 
        nums = []
        for i, point in enumerate(points):
            x = point[0]
            y = point[1]
            distance = sqrt(x**2 + y**2)
            nums.append((distance, i))

        left = 0
        right = len(nums) - 1
        res = []

        def partition(l, r):
            # Pick a pivot index
            pivot_index = random.randint(l, r)
            pivot = nums[pivot_index][0]
            # Swap pivot index with r
            nums[r], nums[pivot_index] = nums[pivot_index], nums[r]
            swap = l
            # Go from l to r and swap any values that is smaller than or equal to the pivot
            for i in range(l, r):
                if nums[i][0] <= pivot:
                    nums[i], nums[swap] = nums[swap], nums[i]
                    swap += 1
            # Swap the pivot with value at swap
            nums[swap], nums[r] = nums[r], nums[swap]
            return swap

        idx = -1
        while left < right:
            part_index = partition(left, right)
            # This means the partition index is the kth value, where all items to the left of it are the closest to the origin.  
            if part_index == k - 1:
                idx = part_index
                break
            elif part_index > k - 1:
                # If the partition index has more than k values to the left of it, we need to move the right pointer.
                right -= 1
            elif part_index < k - 1:
                # If partition index has less than k values to the left of it, we need to move the left pointer
                left += 1
        
        for i in range(0, idx + 1):
            res.append(points[nums[i][1]])
        
        return res

# T: O(N) - on average, it is O(N) with a good pivot selection. It is O(N**2) in the worst case. 
# S: O(N) - we had to copy values to a new array
