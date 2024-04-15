class Solution:
    # Do DFS with memoization
    # We want to pass in the current string into the DFS function.
    # If the string is empty, we can return a list with an empty string.
    # If the string is already in the cache, return the cached value.
    # Otherwise, go through all possible words and see if the current string starts with any. 
    # If they do, we can splice the current string at the length of the word and pass it to DFS. 
    # The DFS then returns all possibilities of subwords so we want to take every one of those and add the current word to the front of it.
    # Then we can return the result. 
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}

        def dfs(curr):
            if not curr:
                return [""]
            if curr in cache:
                return cache[curr]
            res = []
            # Go through every possible word in dict
            for word in wordDict:
                # If the current string starts with it, we can splice it and call DFS on the sub-sentence
                if curr.startswith(word):
                    sub_sentences = dfs(curr[len(word):])
                    # This will return all sentences that can be generated by the sub sentence.
                    for sentence in sub_sentences:
                        # If we see the base case result (empty string), just ignore the sentence
                        if sentence == "":
                            res.append(word)
                        # Otherise, we add a space between word and sentence
                        else:
                            res.append(word + " " + sentence)
            # Cache result before returning
            cache[curr] = res
            return res
    
        return dfs(s)

# K = number of word in dictionary
# N = length of s
# T: O(2^N + N^2) - In the worst case, we have to split at every possible letter if the dictionary contains all letters in the alphabet. 
# We also need to loop through each sentence and do string concatenation, so that is O(N^2)
# S: O(2^N + N^2) - We need to store all the sub sentences and concat them. We also need to cache all possible values. 