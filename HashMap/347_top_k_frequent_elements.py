class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Go through nums and get the # of occurences of each integer. Map int -> freq
        # Go through the values in the map and push them onto the heap until we hit K values.
        # If we are over k values and the value we have is larger than the first value in the heap, pop it and push new value.
        # We only want the numbers in the heap, not the frequency, return that as the result.
        def heap():
            occurences = {}
            heap = []
            # Count the number of occurences of each number
            for num in nums:
                if num in occurences:
                    occurences[num] += 1
                else:
                    occurences[num] = 1
            
            # Go through every number in the map and push it into the heap
            for num in occurences.keys():
                freq = occurences[num]
                # If the heap has less than k values on it, push (freq, num) onto it
                if len(heap) < k:
                    heapq.heappush(heap, (freq, num))
                else:
                    # If we have more than k items, see if this num's freq is larger than the smallest in the heap
                    if freq > heap[0][0]:
                        # If so, pop that off and then add this new item
                        heapq.heappop(heap)
                        heapq.heappush(heap, (freq, num))
            
            # Go through the heap, we only want the num, not the # of occurences
            res = []
            for item in heap:
                res.append(item[1])

            return res  
        # T: O(NlogK)
        # S: O(N)

        # We can also use bucket sort for this, which can be done in linear time.
        # The idea is to create an array that is the same size as the length of nums
        # Each index acts as the # of occurences for each value and the value at the index is a list of numbers.
        # We then go through that list from largest to smallest and add values to our result until we hit k values. 
        def bucket():
            occurences = Counter(nums)
            bucket = [[] for i in range(len(nums) + 1)]
            res = []
            
            # Go through each key and map it to the bucket list
            for key in occurences:
                bucket[occurences[key]].append(key)

            for i in range(len(bucket) - 1, 0, -1):
                for n in bucket[i]:
                    res.append(n)
                    if len(res) == k:
                        return res

            return res
        # T: O(N)
        # S: O(N)
