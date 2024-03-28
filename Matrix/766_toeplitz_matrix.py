class Solution:
    # Go through the entire matrix and make sure that every cell's diagonal top left has the same value.
    # If that cell is out of bounds, we ignore it and move onto the next. 
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        
        def naive():
            # Go through the matrix
            for i in range(m):
                for j in range(n):
                    # If the left diagonal is out of bounds, continue
                    if i - 1 < 0 or j - 1 < 0:
                        continue
                    # If the diagonal left is in bounds and the current value is not equal to it, then we can safely return false
                    if matrix[i][j] != matrix[i - 1][j - 1]:
                        return False
            
            # If we haven't returned false yet, we can return True
            return True
        
        def optimal():
            # In the optimal solution, we would technically only check the values in the first row and then every value in the first column.
            # From there, we check if the diagonal from that cell is Topeplitz. 
            def is_diagonal_equal(r, c):
                val = matrix[r][c]

                # Go until we are out of bounds
                while r < m and c < n:
                    # If the value at this cell is not the same as the first value, then we can return False
                    if matrix[r][c] != val:
                        return False
                    r += 1
                    c += 1
                
                # If we get here, we can return False
                return True
            
            # Go through the first row
            for i in range(n):
                if not is_diagonal_equal(0, i):
                    return False
            
            # Go through the first column
            for j in range(m):
                if not is_diagonal_equal(j, 0):
                    return False
            
            return True
        
        return optimal()
    
# Time Complexity: O(m x n), since we have to go through every cell in the matrix
# Space Complexity: O(1), we don't really store anything. 