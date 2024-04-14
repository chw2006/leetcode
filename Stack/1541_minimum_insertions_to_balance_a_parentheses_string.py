class Solution:
    # Think of it as trying to balance the amount of closing parentheses and opening parentheses.
    # Closings is how many closings we need to keep the string balanced.
    # If we see an opening, increment closings by 2, because 2 closings = 1 opening is the rule.
    # We cannot have an odd number of closings unless we insert. So make it even again with an insertion.
    # If we see a closing, decrement closings. If closings is ever below 0, it means we have too many closings.
    # So insert an opening and increment closings by 2. 
    # Return the closings and insertions, we do that because closings could be odd at the end. 
    def minInsertions(self, s: str) -> int:
        closings = 0
        insertions = 0

        for char in s:
            if char == '(':
                # For every opening, we need 2 closings
                closings += 2
                # If closings is odd, make it even again by inserting 
                if closings % 2:
                    # Make closings even
                    closings -= 1
                    # With this insertion
                    insertions += 1
            else:
                # For every closing, decrement closing.
                closings -= 1
                # If closings is less than 0, it means we no longer need closings, we need openings.
                # So insert an opening to increase the number of closings we need. 
                if closings < 0:
                    closings += 2
                    insertions += 1
            
        return closings + insertions

# T: O(N)
# S: O(1)