class Solution:

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # This solution is sub-optimal, binary search is much more efficient. 
        # We need to traverse the matrix
        # We add each matrix value into a maxheap that is size k
        # MaxHeap means the largest values are at the top
        # If the heap has k values and the value we want to push is less than the top of the heap, pop from the heap and push the new value.
        # At the end of the traversal, the top value of the heap should be the kth smallest. 
        def heap():
            n = len(matrix)
            # We want to build a maxHeap, so all values are pushed in as negative. 
            heap = []
            for r in range(n):
                for c in range(n):
                    # Check if the heap is at capacity
                    if len(heap) >= k:
                        # We need to evict from the heap if the value is smaller than the top
                        if matrix[r][c] < -heap[0]:
                            # Evict the largest value
                            heapq.heappop(heap)
                            # Push the new value
                            heapq.heappush(heap, -matrix[r][c])
                    else:
                        # If we are below size k, add to heap
                        heapq.heappush(heap, -matrix[r][c])
            
            # Return the top value in the heap
            return -heap[0]
        # T: O(N * logK): We have to iterate through the matrix and heap push and heap pop onto the heap, which is logK. 
        # S: O(K): We have to keep K elements in the heap. 
        
        def binary_search():
            # Start at left = 0,0 and right at (n - 1), (n - 1)
            # Find the middle value between these 2.
            # Find the number of values that are less ore equal to this value
            # If that value is larger than k, then we need to go left.
            # If it is smaller than k, we need to go right. 
            n = len(matrix)
            left = matrix[0][0]
            right = matrix[n - 1][n - 1]

            # Count the amount of values smaller than x
            def countLessOrEqual(x):
                count = 0
                # Start at rightmost column
                col = n - 1
                # For each row, start at the last value until we reach col = 0.
                for row in range(n):
                    # Find values that are bigger than x.
                    # If there are, decrement the column so we don't look in that column anymore for subsequent rows
                    while col >= 0 and matrix[row][col] > x:
                        col -= 1
                    # The less values bigger than x, the more cols we count. 
                    count += (col + 1)
                return count

            # Do Binary search on the matrix
            while left < right:
                mid = left + (right - left) // 2
                # If there are more than k values smaller, go left. 
                if countLessOrEqual(mid) >= k:
                    right = mid
                # Otherwise go right
                else:
                    left = mid + 1
            
            return left
        
        return binary_search()

        # T: O(N * logD). Where D is the difference beween the min and max values in the matrix and N is the length/width of the matrix.
        # S: O(1) we don't store anything besides pointers and counters. 
