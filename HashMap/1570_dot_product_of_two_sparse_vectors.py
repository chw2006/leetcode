
# This problem requires us to calculate the product of 2 sparse vectors efficiently.
# Because sparse vectors have a lot of 0s, we can simply not store them
# Instead we store the non-zero values in a map.
# When calculating the dot product of the 2 vectors, we only care if 2 indicies are both populated in the maps. 
# If only one vector is sparse, it is actually irelevant to the problem if we only search through the shorter map.
# In this case, the shorter vector is the only one that matters since the longer vector would end up mulitplying by 0 most of the time. 
class SparseVector:
    # Constructor: turn nums into a sparse vector instance
    def __init__(self, nums):
        self.map = {}
        # Go through nums and store non-zero values into a map
        for i in range(len(nums)):
            if nums[i] > 0:
                self.map[i] = nums[i]
    
    # Calculate the dot product between this vector and vec
    def dotProduct(self, vec):
        # Get the map from vec
        vec_map = vec.map
        product = 0
        smaller = {}
        larger = {}
        # Find out which map is smaller. We want to iterate through the smaller one.
        if len(self.map) < len(vec_map):
            smaller = self.map
            larger = vec_map
        else:
            smaller = vec_map
            larger = self.map
        # Go through the smaller map, this makes the fuction more efficient. 
        # In the instance where one vector is sparse and one is not, going through the smaller one will make the non sparse vector irelelvant. 
        for k in smaller.keys():
            if k in larger:
                product += smaller[k] * larger[k]
        return product

nums1 = [0,1,0,0,2,0,0]
nums2 = [1,0,0,0,3,0,4]

v1 = SparseVector(nums1)
v2 = SparseVector(nums2)

print(v1.dotProduct(v2))

# T: O(N) for constructor. If K = # of non-zero values, then dotProduct is O(K).
# S: O(N) for both, we make copies of both maps for dotProduct. 

