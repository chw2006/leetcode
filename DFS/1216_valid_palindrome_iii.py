class Solution:
    # Solve with memoization and recursive solution.
    # We keep the left, right pointers and removes in the DFS function.
    # The base case is if ever removes is larger than k, we have to return false.
    # If left and right ever cross, we can return True. It means we've gone over every character in the string.
    # We can memoize the result of every triplet. So before calling anymore recursion, check if we already did this work before.
    # If left and right are equal, call DFS with incremented pointers.
    # If they are not, we must call DFS with either pointer changed, because we do not know which one to change.
    # If either returns True, then we will return True. Cache the value before returning. 
    def isValidPalindrome(self, s: str, k: int) -> bool:
        cache = {}
        def dfs(left, right, removes):
            # Base case: if removes is ever larger than k, we have to return False
            if removes > k:
                return False
            # When right and left meet, we can return True
            if right <= left:
                return True
            if (left, right, removes) in cache:
                return cache[(left, right, removes)]
            res = False
            # If left and right are equal, move on to next chars
            if s[left] == s[right]:
                res = dfs(left + 1, right - 1, removes)
            else:
                # If not, we don't know removing which character works better, so we try both.
                # If either reach the end, we can return True
                res = dfs(left, right - 1, removes + 1) or dfs(left + 1, right, removes + 1)
            cache[(left, right, removes)] = res
            return res
        
        return dfs(0, len(s) - 1, 0)
# T: O(K*N^2) - We have to go through k * N^2 states. 
# S: O(K*N^2) - We have to store k * N^2 states in the cache. 