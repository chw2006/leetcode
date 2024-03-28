class Solution:
    # We need to keep track of the last word seen and the current word
    # Go through the string, if we see a space and we've seen a word, set it to lastword and reset current.
    # Otherwise, append the char to current.
    # After the loop, to account for the case of the string not ending with a space, if curr is non-empty, set it to lastword.
    # Return the length of lastword.
    def lengthOfLastWord(self, s: str) -> int:
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