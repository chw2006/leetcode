class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # Need to use 2 pointers to traverse both intervals.
        # The condition we check to see if 2 intervals overlap is if the min of the 2 ends is larger or equal to the max of the 2 starts. 
        # If we have an intersection, we want to add (max(starts), min(ends) to the result.
        # Regardless of intersection, we need to see which pointer we increment.
        # We always want to increment the pointer that has a smaller end time. 
        # If one list is longer than the other, we only go until the smaller list is exhausted. 

        p1 = 0
        p2 = 0
        res = []

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            # We have an intersection
            if min(end1, end2) >= max(start1, start2):
                res.append([max(start1, start2), min(end1 ,end2)])
            
            # Increment the pointer that's been exhausted (shorter end)
            if end2 > end1:
                p1 += 1
            else:
                p2 += 1
        
        return res
    
    # T: O(N + M)
    # S: O(N + M)
