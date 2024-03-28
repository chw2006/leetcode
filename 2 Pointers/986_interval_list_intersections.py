class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # There are 2 basic cases to consider.
        # Where the 2 sets are completely distjoint (no overlap), we just want to skip to the next values in the list.
        # When there is an intersection, we want to add to the result. 
        # The intersection is the max of the starts and the min of the ends. 
        # If end1 > end2, increment p2
        # Otherwise, increment p1

        p1 = 0
        p2 = 0
        intersections = []

        while p1 < len(firstList) and p2 < len(secondList):
            start1, end1 = firstList[p1]
            start2, end2 = secondList[p2]

            # Disjoint cases
            # If B starts after A ends, we need to increment A. 
            if start2 > end1:
                p1 += 1
            # If A starts after B ends, we need to increment B. 
            elif start1 > end2:
                p2 += 1
            # Intersection case
            else:
                # If the 2 intervals intersect, we always take the max of the start and the min of the end. Because the intersection is always the contained block. 
                intersections.append([max(start1, start2), min(end1, end2)])
                # For overlap case. If 1 ends after 2, only increment p2. 
                if end1 > end2:
                    p2 += 1
                # If 2 ends after 1, increment p1. 
                else:
                    p1 += 1
            
        return intersections
                