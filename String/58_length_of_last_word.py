class Solution:
    # We need to keep track of the last word seen and the current word
    # Go through the string, if we see a space and we've seen a word, set it to lastword and reset current.
    # Otherwise, append the char to current.
    # After the loop, to account for the case of the string not ending with a space, if curr is non-empty, set it to lastword.
    # Return the length of lastword.
    def lengthOfLastWord(self, s: str) -> int:
        # O(N) space solution
        def linear():
            lastword = []
            curr = []

            for i in range(len(s)):
                if s[i] == " ":
                    if len(curr) > 0:
                        # If we see a space, we have to save the last word we've seen
                        lastword = curr
                        # Reset curr to prepare for new words
                        curr = []
                else:
                    curr.append(s[i])
            
            # Edge case in that the string doesn't end with any spaces
            # If curr is non-empty, we have to return that as the last word
            if len(curr) > 0:
                lastword = curr
            
            return len(lastword)
        # T: O(N) have to go through the entire string once.
        # S: O(N) have to keep the current word and the last word. 

        # O(1) space solution
        # Keep track of the current count and the count of the last word. 
        # Go through the string, if the character is a letter, increment count. If it's a space, save the last count if count > 0.
        # Then reset count to 0.
        # At the end, if count is still 0, return last_count. 
        # Otherwise, return count. 
        def constant():
            count = 0
            last_count = 0
            # Go through string
            for char in s:
                # If char is alphabetical, increment count
                if char.isalpha():
                    count += 1
                # If it's a space and count > 0, save count to last_count
                else:
                    if count > 0:
                        last_count = count
                    # Reset count to 0
                    count = 0

            # If count is 0, that means the string ended in spaces, so we need to use last_count
            if count == 0:
                return last_count
            # If count is > 0, then we can just return it. 
            else:
                return count
        
        # T: O(N) - have to go through the entire string
        # S: O(1) - we only use 2 counters
