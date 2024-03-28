class Solution:
    # Use DFS backtracking for this
    # We need to keep track of how many left and right parentheses we have
    # We also need to keep track of the longest string we've seen. 
    # We also need to keep track of the result in a set (since the results are unique)
    # For the DFS function, we need to keep track of the left and right parentheses, the current index, and the result. 
    # The base case is when we reach the end of the string (index == len(str)) and the amount of left and right parentheses is the same.
    # In that case, we need to know if this string is the longest possible. If it is, then we need to reset our result and only add this one to it. 
    # If it is equal to the longest string, add this string to the result set.
    # We can decide to either take or not take a left parentheses
    # We can only take a right parentheses when left < right. In that case, we can decide to take it or not to take it. 
    # We have to take non () characters as-is. 
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.longest_string = -1
        self.res = set()

        def dfs(i, curr_res, lp, rp):
            # base case
            # If we are at the end of the string and the left and right parens are equal, then we have a valid string
            if i >= len(s):
                if lp == rp:
                    # Since we have a valid result, we need to check if it's the longest yet
                    if len(curr_res) > self.longest_string:
                        self.longest_string = len(curr_res)
                        # Empty the set since we now have a new longest string
                        self.res = set()
                        self.res.add("".join(curr_res))
                    elif len(curr_res) == self.longest_string:
                        # Add current result to result
                        self.res.add("".join(curr_res))
            # If we are not at the end of the string, process it
            else:
                # 3 Cases, we have a '(', a ')', or a letter.
                c = s[i]
                # If we have an opening, we can either add it or not add it
                if c == '(':
                    # Include this
                    curr_res.append(c)
                    # Call DFS
                    dfs(i + 1, curr_res, lp + 1, rp)
                    # Backtrack and remove this from the string
                    curr_res.pop()
                    # Don't include this
                    dfs(i + 1, curr_res, lp, rp)
                elif c == ')':
                    # We can include or don't include the closing. We can only include if lp > rp
                    # Don't include
                    dfs(i + 1, curr_res, lp, rp)
                    # We can only add this if lp > rp. Otherwise, the string will never be valid afterwards.
                    if lp > rp:
                        # Include this
                        curr_res.append(c)
                        dfs(i + 1, curr_res, lp, rp + 1)
                        # Backtrack and don't include this
                        curr_res.pop()
                else:
                    # Case of a non () char
                    # Add it to the result
                    curr_res.append(c)
                    # We have to include it
                    dfs(i + 1, curr_res, lp, rp)
                    # Backtrack
                    curr_res.pop()
        
        dfs(0, [], 0, 0)

        return list(self.res)

# Time Complexity: O(2^N) since we are making 2 decisions for every value, worst-case. 
# Space Complexity: O(N) since we are storing the results. 