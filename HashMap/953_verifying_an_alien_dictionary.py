class Solution:
    # Map the letter to its order
    # Compare 2 words, check if the first word's letter comes before the 2nd. 
    # If not, then we can return false.
    # Also, if 2 words have the same word in them but the 2nd word is shorter than the first, we have to return false.
    # Because you cannot compare the letter from word1 to no letter. 
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # If there's 1 or no word in words, return True
        if len(words) <= 1:
            return True

        # Create the alphabet order mapping
        alphabet = {}
        for i, c in enumerate(order):
            alphabet[c] = i
        
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            # We only want to compare up to the length of word1 since word2 cannot share a prefix and be shorter than word1. 
            for j in range(len(word1)):
                # Word 2 cannot be shorter than word 1 while having the same prefix. 
                if j == len(word2):
                    return False
                if word1[j] != word2[j]:
                    # Word 2 cannot have a letter with a lower order than word 1
                    if alphabet[word2[j]] < alphabet[word1[j]]:
                        return False
                    # If the 2 words do not equal, but are in order, we need to break out of the interior loop
                    break
        return True

# T: O(M) where M is the length of the sum of all the words in the array. 
# S: O(1) since we only store 26 letters in a map, it's constant space. 
