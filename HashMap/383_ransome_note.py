from collections import Counter


class Solution:
    # Create a map of occurences of each letter in magazine.
    # Then go through each char in ransomNote.
    # If the char is not in the map, return False.
    # If it is in the map, its occurences needs to be larger than 0. If not, return False.
    # If its occurences is larger than 0, decrement the value in the map. 
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Put # of occurences of each char from magazine.
        map = Counter(magazine)

        # Go through each char in ransome note
        for c in ransomNote:
            # If it is in the map, we need to make sure that it has more than 0 occurences.
            if c in map:
                # If it does, decrement its count
                if map[c] > 0:
                    map[c] -= 1
                # If there are 0 occurences, we have to return False
                else:
                    return False
            # If string not in map, return False
            else:
                return False
        
        return True

# T: O(N)
# S: O(M) - where M is the # of unique chars in magazine. 