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

# Time Complexity: O(N * logN). Heapify takes worst case O(NlogN). 
# Space Complexity: O(N). We store all items in a heap and then k items in the result. Worst case O(N)