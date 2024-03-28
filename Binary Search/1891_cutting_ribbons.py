# We know a range of possible values for the lengths
# That's because the length cannot be larger than the max value in the array.
# So we can start at 1 for left, since 1 is the min length, and max(ribbons) for right. 
# We then do a binary search on that range. 
# We determine if a ribbon of that length can be cut into k ribbons using can_cut()
# can_cut() simply goes through every ribbon and finds out how many cuts of that length we can make.
# If it can cut, then we search for a larger value, i.e. increment left to mid + 1.
# If we cannot, then we search for a smaller value, i.e. decrement right to mid - 1. 
# The max value will eventually be contained in the right pointer. 
def cutting_ribbons(ribbons, k):
    left = 1
    right = max(ribbons)

    # Go through the ribbons and see how many cuts of length we can make.
    def can_cut(length):
        cuts = 0
        for ribbon in ribbons:
            cuts += ribbon // length
        # If we can cut more or equal to k times, return true
        if cuts >= k:
            return True
        else:
            return False
    
    # Go until the left and right pointers meet
    while left <= right:
        # Find mid, important: use () around left + right
        mid = (left + right) // 2
        # We can cut for this length, so try looking for a larger one. 
        if can_cut(mid):
            left = mid + 1
        # We cannot cut for this length, try a smaller value
        else:
            right = mid - 1

    return right


test = [9, 7, 5]
length = cutting_ribbons(test, 3)
print(length)

#T: O(NlogK) since we are using binary search, but have to go through all ribbons on every search. 
#S: O(1)