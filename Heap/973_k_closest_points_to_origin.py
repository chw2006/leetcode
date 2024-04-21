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

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            # Generate the distance of each point to the origin. Place them in a max heap with vals as tuples (-distance, index)
            # To calculate euclidean distance, use sqrt(x**2 + y**2). 
            # Use maxHeap. Push onto heap as negative values. If heap gets larger than size k, pop from it. 
            heap = []
    
            # Get distances and push into maxheap
            for i, point in enumerate(points):
                x = point[0]
                y = point[1]
    
                distance = sqrt(x**2 + y**2)
                # Push onto heap
                heapq.heappush(heap, (-distance, [x, y]))
                # If size of heap is ever larger than k, pop its largest value
                if len(heap) > k:
                    heapq.heappop(heap)
    
            # Return only the points in the heap
            return [point for _, point in heap]
    
    
# T: O(NlogK)
# S: O(N)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use Quickselect, which is O(N) with random pivot selection and O(1) space.
        # Quickselect starts with 2 pointers, each at the end of the array.
        # Find the partition index based on the range we are given.
        # If partition index is equal to k, return all values prior to k. 
        # If the partition index > k, that means we have more than k elements smaller than the partition index, so move left (right = index - 1)
        # If partition index < k, that means we need to move right (left = index + 1)
        # To find partition index, generate a random pivot. 
        # Swap pivot element and right-most element. 
        # Keep a swap pointer starting at 0.
        # Go from left to right, and compare each value to the pivot. If a value is smaller or equal to the pivot, move it to the swap index and increment swap index. 
        # After swapping is done, swap the pivot value (to right of array) with the swap index value. Because swap points at the first element larger than pivot. 
        # Return swap as partition index. 

        # Calculate the distance between this point and the origin
        def getDistance(point):
            x = point[0]
            y = point[1]
            distance = sqrt(x**2 + y**2)
            return distance

        # Find the partition index
        def partition(left, right):
            swap = left
            pivot_idx = random.randint(left, right)
            pivot = points[pivot_idx]
            pivot_distance = getDistance(pivot)
            # Swap pivot and right
            points[right], points[pivot_idx] = points[pivot_idx], points[right]
            for i in range(left, right):
                distance = getDistance(points[i])
                # Swap current and swap
                if distance <= pivot_distance:
                    points[swap], points[i] = points[i], points[swap]
                    swap += 1
            # Swap swap and pivot
            points[swap], points[right] = points[right], points[swap]
            return swap

        # Do quickselect
        left = 0
        right = len(points) - 1
        while left < right:
            partition_idx = partition(left, right)
            if partition_idx == k:
                break
            if partition_idx > k:
                right = partition_idx - 1
            elif partition_idx < k:
                left = partition_idx + 1
        
        return points[:k]

# T: O(N) in the average case. O(N**2) in the worst case, but we have a random pivot so we should be fine. 
# S: O(1)
