class Solution(object):
    # This is a pretty basic combination problem. 
    # We need to map every digit to a letter list. 
    # We use a backtracking algorithm to come up with every letter combination for every digit. 
    # The base case to return is if our combo is the same length as the digits string.
    # Otherwise, we get the letters for that digit and loop through every letter of every other digit.
    # After that's done for that letter, we remove that letter (backtrack) and add the next letter as the first digit and repeat the process. 
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # Create a hash map for digit to letters
        phoneMap = {}
        phoneMap['2'] = ['a', 'b', 'c']
        phoneMap['3'] = ['d', 'e', 'f']
        phoneMap['4'] = ['g', 'h', 'i']
        phoneMap['5'] = ['j', 'k', 'l']
        phoneMap['6'] = ['m', 'n', 'o']
        phoneMap['7'] = ['p', 'q', 'r', 's']
        phoneMap['8'] = ['t', 'u', 'v']
        phoneMap['9'] = ['w', 'x', 'y', 'z']

        results = []

        def dfs(i, currCombo):
            # Base case, the combo must be the same length as the digits string.
            if len(currCombo) == len(digits):
                # In that case, add this combo to the results
                results.append(currCombo)
                return
            # Make sure we are in bounds
            if i >= len(digits):
                return
            # Get the letters array for this digit
            letters = phoneMap[digits[i]]
            # Go through every letter for this digit
            for j in range(len(letters)):
                # Add this letter to the combo
                currCombo += letters[j]
                # Call DFS on the next digit
                dfs(i + 1, currCombo)
                # Backtrack by removing the last character
                currCombo = currCombo[:-1]
        # Call DFS
        if digits:
            dfs(0, "")
        return results

# T: O(4^N) - Because we can have at most 4 letters per number which is 4 different dfs calls. 
# S: O(4^N) - Because we store the combos for each DFS call
