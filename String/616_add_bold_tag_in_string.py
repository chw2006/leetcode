def addBoldTag(s, words):
    # Use a bold array to indicate whether or not we need to bold the char at each index
    # Go through every word in words, and find where the yare in s. Then set every instance of it to True in the bold array. 
    # Go through the string, add a bold tag to the start of every true portion of the string. When it is no longer true, add a closing. 
    
    bold_status = [False] * len(s)

    for word in words:
        # Find where the word is in s
        start = s.find(word)
        length = len(word)
        # Find all instances of the word is in s
        while start != -1:
            # Set T for every index of this word
            for i in range(start, start + length):
                bold_status[i] = True
            # See if there is this word in the rest of s
            start = s.find(word, start + 1)
        
    sb = []
    i = 0
    # Go through s and if we hit a bold status = true, insert a bold tag. 
    while i < len(s):
        if bold_status[i]:
            # Add the bold tag
            sb.append("<b>")
            # Keep going until we hit bold_status = False
            while i < len(s) and bold_status[i]:
                sb.append(s[i])
                i += 1
            # Add the closing tag
            sb.append("</b>")
        # Add the char as is
        else:
            sb.append(s[i])
            i += 1
    
    return ''.join(sb)

print(addBoldTag("aaabbcc", ["aaa", "aab", "bb"]))
print(addBoldTag("aaabbcc", ["aaa", "aab", "bc"]))
print(addBoldTag("aaabbcc", ["aaa", "aab", "bb", "cc"]))
print(addBoldTag("abcxyz123", ["abc", "123"]))

        
            
