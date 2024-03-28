class Solution:
    # We need to use backtracking with memoization for this problem. 
    # The base case is when both strings are at the end and the difference between their pointers is 0. Then return true
    # There are numerous cases we need to take care of. There is the case of when we see a number for either string
    # In this case, we don't know if the number is just one digit or multiple digits after that, so we have to try them all, which is where backtracking comes in.
    # When both chars in the strings are letters, we compare them. If the diff is 0 and they are equal, move i and j to the next. 
    # If the diff is < 0, increase the pointer for the 2nd string and add 1 to the diff. 
    # If the diff is > 0, increase the pointer for the 1st string and subtract 1 from the diff. 
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        cache = {}

        def dfs(i, j, d):
            # Base case
            if i == n and j == m:
                if d == 0:
                    return True
                else:
                    return False
            # Memoization
            if (i, j, d) in cache:
                return cache[(i, j, d)]
            # Case of digits for s1
            if i < n and s1[i].isdigit():
                k = i
                num = 0
                # Go until we do not hit a digit. Then for every possible number, call DFS to see if that is possible. 
                while k < n and s1[k].isdigit():
                    num = (num * 10) + int(s1[k])
                    k += 1
                    # Do a recursive call on this num, do d - num so we can tell which string ptr to increment later
                    if dfs(k, j, d - num):
                        return True
            # Case of digits for s2
            elif j < m and s2[j].isdigit():
                k = j
                num = 0
                # Go until we do not hit a digit. Then for every possible number, call DFS to see if that is possible. 
                while k < m and s2[k].isdigit():
                    num = (num * 10) + int(s2[k])
                    k += 1
                    # Do d + num, so it's the opposite of what's there for s1
                    if dfs(i, k, d + num):
                        return True
            # Case where diff is 0 and they are alpha
            elif d == 0:
                # If they are equal and alpha, then move to next chars
                if i < n and j < m and s1[i] == s2[j]:
                    return dfs(i + 1, j + 1, d)
            # Case where they are alpha and the diff is less than 0
            elif d < 0:
                # If diff is less than 0, that means that s1 is ahead of s2. So we need to increment s2 and diff. 
                if j < m:
                    return dfs(i, j + 1, d + 1)
            elif d > 0:
                # If diff is larger than 0, that means s2 is ahead of s1. Increment s1 and decrement diff
                if i < n:
                    return dfs(i + 1, j, d - 1)
            
            # If we get here, then we can cache that for this tuple, the strings are not equal.
            cache[(i, j, d)] = False
            return False

        return dfs(0, 0, 0)