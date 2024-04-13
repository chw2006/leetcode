class Solution:
    # Put initial k values onto heaps
    # Keep a left and right heap. Left heap is a max heap (pop biggest values) and right heap is min heap (pop smallest values)
    # Go through first k elements and add to heap. Always add to left heap first and then balance if needed.
    # Our stipulation is that if k is odd, the left heap always contains the median. Find median for first k values.
    # Keep a hash map for values that are going out of the window. The value going out of the window is at i - k. 
    # How we push onto the heaps depends on the current num and the current balance.
    # If balance is negative, it means to add to the left heap.
    # If balance is positive, it means to add to the right heap.
    # After adding, we need to keep the balance 0, so pop and push accordingly. 
    # If any elements in the remove map are at the top of the heaps, pop them and decrement the value in the map. 
    # Add median to result.  
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # Left heap keeps the all values to the left of median (smaller or equal)
        left_heap = []
        # Right heap keeps all values larger than the median
        right_heap = []
        remove_map = defaultdict(int)
        res = []

        # If k is odd, median is always at top of left heap.
        # If k is even, median is the top of both heaps added and divided by 2. 
        def get_median():
            if k % 2:
                return -left_heap[0]
            else:
                return (-left_heap[0] + right_heap[0]) / 2

        # Go through the first k values and add onto the 2 heaps
        for i in range(k):
            num = nums[i]
            # Add onto left heap first
            heapq.heappush(left_heap, -num)
            # Pop the largest value from left and put it onto right
            heapq.heappush(right_heap, -heapq.heappop(left_heap))
            # If right heap is larger than left heap, push onto left heap
            # The limitation is that the left heap is always larger when we have an odd sized window
            if len(right_heap) > len(left_heap):
                heapq.heappush(left_heap, -heapq.heappop(right_heap))
    
        # Get median for initial window
        median = get_median()
        res.append(median)
        
        # Go through the rest of the window
        for i in range(k, len(nums)):
            num = nums[i]
            left_num = nums[i - k]
            remove_map[left_num] += 1
            # Balance = 0, both are balanced
            # Balance = 1, right heap needs an extra value
            # Balance = -1, left heap needs an extra value
            balance = 1
            # The median is always in the left heap. So if the number we are removing is smaller than the median,
            # It means it's to the left of the median in the array. 
            # So the left heap will need an extra element since the left_num will be removed from it.
            if left_num <= median:
                balance = -1
            # Add to the heap depending on balance
            if num <= median:
                # If num is smaller or equal to median, add to the left heap
                balance += 1
                heapq.heappush(left_heap, -num)
            else:
                # If num is larger than median, it goes to the right heap. 
                balance -= 1
                heapq.heappush(right_heap, num)
            # Rebalance
            if balance < 0:
                # If balanced is less than 0, it means that left heap needs more elements
                heapq.heappush(left_heap, -heapq.heappop(right_heap))
            elif balance > 0:
                heapq.heappush(right_heap, -heapq.heappop(left_heap))
            
            # Remove values that are out of the window, but only if they are at the top of the heap
            while left_heap and remove_map[-left_heap[0]] > 0:
                remove_map[-left_heap[0]] -= 1
                heapq.heappop(left_heap)
            
            while right_heap and remove_map[right_heap[0]] > 0:
                remove_map[right_heap[0]] -= 1
                heapq.heappop(right_heap)
            
            # Get the median
            median = get_median()
            res.append(median)

        return res

# T: O(NlogK) - Must pop or push onto a heap with K elements at least N times. 
# S: O(K) - Heaps have k values on them. Result is O(N/K) since it depends on how many windows of K there are in the window. 