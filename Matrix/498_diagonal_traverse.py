class Solution:
    # Start by going up
    # When going up, row - 1, col + 1. 
    # When row goes out of bounds (smaller than 0), row + 1
    # When col goes out of bounds (col > n), row + 2, col - 1
    # When we reach out of bounds, go down.
    # When going down, row + 1, col - 1. 
    # When row goes out of bounds (row > m), row - 1, col + 2
    # When col goes out of bounds (col < 0), col + 1
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        res = []
        up = True
        row = 0
        col = 0
        
        # Go until we vist every coordinate
        while len(res) != m * n:
            if up:
                while row >= 0 and col < n:
                    # Add this to the result first
                    res.append(mat[row][col])
                    # Go up, row - 1, col + 1
                    row -= 1
                    col += 1
                # If col is out of bounds, we have to add 2 to row and subtract col by 1
                if col == n:
                    row += 2
                    col -= 1
                # If row is out of bounds, just add 1 to row
                else:
                    row += 1
                # Since we know that we are out of bounds, we have to go down now. Set up to false. 
                up = False
            else:
                while col >= 0 and row < m:
                    res.append(mat[row][col])
                    # When going down, add 1 to row and subtract from col
                    row += 1
                    col -= 1
                # If the row is out of bounds, add 2 to col and subtract row by 1.
                if row == m:
                    row -= 1
                    col += 2
                # If the col is out of bounds, add 1
                else:
                    col += 1
                # We know that we are out of bounds, so reverse direction. 
                up = True
        
        return res
    
    # T: O(N) since we go through every cell
    # S: O(N) since we store the result