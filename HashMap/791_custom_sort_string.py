def custom_sort_string(order, s):
    # Use a hash map to keep track of the # of occurences of each letter
    # Add the characters in order to the string first, remove them from the map once you've added them
    # After those have been added add the chracters that weren't in order.

    map = {}
    result = ""

    # Create a hash map of the number of occurences of each char
    for c in s:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1

    # Add the chars from order to the string 
    for c in order:
        # Add this letter to the result 
        for i in range(map[c]):
            result += c
        # Remove c from the map so we don't add it again later
        map.pop(c)
    
    # Add the rest of the chars that aren't in order to the string
    for c in map:
       for i in range(map[c]):
            result += c
    
    return result

    

print(custom_sort_string("cba", "aabcccdfg"))

# T: O(N)
# S: O(N)