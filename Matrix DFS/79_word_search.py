class Solution:
    # We need to go through every cell in the grid and see if that can be the starting point of the word.
    # For each cell, we call DFS. If any DFS returns true, we return True. 
    # We need to keep track of the row, column, and the index we're at in the string
    # We need to keep a visited set so we can backtrack and don't use the same cells in a word.
    # The base case is if we are at the end of the string index, we can return True.
    # Another base case is that if r, c is out of bounds or has been visited or isn't equal to the current char, we have to return False.
    # If it is equal to the char in word, we increment i and add it to visited. 
    # We then call DFS on the neighbors of this node with the index. 
    # Afterwards, we remove this node from visited to backtrack. 
    # We then return the or of all neighbors. 
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = set()

        def dfs(r, c, i):
            # If we've managed to reach the end of the string, that means the word exists in the matrix. Return true. 
            if i >= len(word):
                return True
            # If we're out of bounds or visited, return False
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited or board[r][c] != word[i]:
                return False

            # Increment i (because we know this position equals what's in the word at i)
            i += 1
            visited.add((r, c))
            # Visit the neighbors
            left = dfs(r, c - 1, i)
            up = dfs(r - 1, c, i)
            right = dfs(r, c + 1, i)
            down = dfs(r + 1, c, i)
            # Backtrack
            visited.remove((r, c))

            return left or up or right or down
    
        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        
        return False

# T: O(n * m * 4^n) - We have to go through a loop of m * n, then for each iteration in the loop, we have to do DFS, which is 4 ^ n. 
# S: O(m * n) since we keep a visited set and have stack frames. 
