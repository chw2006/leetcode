# For this problem, we have to calculate the difference between each character in the string to find the pattern.
# We can store that pattern into a hash map as a tuple and add any strings that fit the pattern to that tuple key.
# We must account for wrap-around, so we mod the difference by 26. 
# We then return the values of the map as a list. 
def groupStrings(strings):
    map = {}
    res = []
    # Go through each string and calculate the separation between each char
    for s in strings:
        if len(s) == 1:
            if -1 in map:
                map[-1].append(s)
            else:     
                map[-1] = [s]
        else:
            tl = []
            # Go through every char in the string starting from the 2nd one
            for i in range(1, len(s)):
                # Calculate the difference between the characters. Need to mod 26 to account for wrap-around
                cur = (ord(s[i]) - ord(s[i - 1])) % 26
                # Add the current difference to the difference list
                tl.append(cur)
            # Put the tuple in the map and add the string
            t = tuple(tl)
            if t in map:
                map[t].append(s)
            else:
                map[t] = [s]
    
    return list(map.values())

print(groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))

