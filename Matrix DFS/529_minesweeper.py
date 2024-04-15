class Solution:
    # We need to take the click coordinate and update the board based on what is at that coordinate.
    # If that square is a Mine, change the coordinate to X and the game is over. 
    # If that square is empty, change it to a B. Then reveal all its adjacent squares that are not bombs recursively using DFS. 
    # If the empty square has at least one adjacent mine, change it to a digit representing number of adjacent mines
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if not board:
            return board
        rows = len(board)
        cols = len(board[0])
        r = click[0]
        c = click[1]
        curr = board[r][c]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]

        # This helper counts the number of mines in adjacent squares
        def count_mines(r, c):
            count = 0
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                # If it's out of bounds, we skip it
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                if board[nr][nc] == 'M':
                    count += 1
            return count
        
        # Clicks are only supposed to be unrevealed squares
        if curr == 'M':
            # If this square is a mine, we change it to an X and the game is over.
            board[r][c] = 'X'
            return board
        elif curr == 'E':
            # If the current square is empty there are 2 possibilities. 
            # There are mines in adjacent squares
            # Change the its number to the number of mines in adjacent squares.
            mines = count_mines(r, c)
            if mines > 0:
                board[r][c] = str(mines)
            # If there are no adjacent mines (all adjacent spaces are blank)
            # Then change this to B and reveal all adjacent blanks
            else:
                board[r][c] = 'B'
                # Need to reveal other blanks for the entire board
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    # If it's out of bounds or a bomb, skip it. 
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc] == 'B':
                        continue
                    # Call updateBoard on the new clicks
                    self.updateBoard(board, [nr, nc])
        
        return board

# T: O(M * N) - Worst case we would have to visit every cell in the board that is not a bomb. 
# S: O(M * N) - We'd have to recursively reveal every square, and give it a reference to the board. 
