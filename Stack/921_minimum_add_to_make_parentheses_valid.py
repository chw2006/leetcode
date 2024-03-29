class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Can be done in O(1) space!
        # Instead of using a stack, just use a separate counter for openings.
        # When we see a closing parentheses, decrement openings if it's above 0.
        # Otherwise, increment moves.
        # At the end of the loop, add remaining openings to moves.
        openings = 0
        moves = 0
        for c in s:
            if c == '(':
                openings += 1
            else:
                if openings > 0:
                    openings -= 1
                else:
                    moves += 1
        
        moves += openings
        
        return moves

# T: O(N) - Need to traverse entire string
# S: O(1) - Only used 2 counters