
class TicTacToe:
    # Keep track of the number of rows/cols, the sum of each row/col and the sum of diagonal and anti-diagonal
    def __init__(self, n: int):
        # Keep count of the sum in each row and column
        # Also keep count in the diagonal and anti-diagonal sums
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti = 0
    # T: O(1)
    # S: O(N)
    
    # The approach is we look at the sum of each row col, diag, anti-diag after the current move and see if any of them tally up to n or - n.
    # Player 1 adds 1 and player 2 subtracts 1 from the sum. So if player 1 wins, the row/col would be +n. Player 2 would be -n. We use abs to avoid checking for positive/negative.
    # We increment the sum by the current player for the current row and col. If row = col, we also have to check diagonals.
    # Also if row == n - cols - 1, we have to check the anti diagonal as well. 
    # If the absolute value of any of these is equal to n, current player wins. Otherwise, no player wins yet. 
    def move(self, row: int, col: int, player: int) -> int:
        # If player is 1, set curr_player to 1
        curr_player = 1
        # If player is 2, set curr_player to -1
        if player == 2:
            curr_player = -1

        # For the row and column the player makes a move in, increment it by curr_player
        self.rows[row] += curr_player
        self.cols[col] += curr_player

        # If row and col equal to each other, those are all the diagonal cells
        # Check diagonal if row = col
        if row == col:
            self.diag += curr_player
        
        # The way to check for anti-diagonal is if the row is equal to n - 1 - col (minus 1 is accounting for 0-indexed)
        if row == self.n - col - 1:
            self.anti += curr_player
        
        # Take the absolute value of the rows, cols, diag, anti-diag and see if they equal n. If any of them do, current player wins. 
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or abs(self.diag) == self.n or abs(self.anti) == self.n:
            return player
        
        # Otherwise, no player wins yet
        return 0

    # T: O(1)
    # S: O(1)