def findRLEArray(encoded1, encoded2):
    # Doing it the way the problem describes it is way too inefficent, there is a 2 pointer solution
    # That can achieve this in one pass. 
    # Go through both arrays at the same time.
    # If the frequency is the same, multiply the values and add to result. Increment i and j. 
    # If the frequencies are not the same, take the min of the 2.
    # Increment the pointer of the smaller frequency. 
    # Set the frequency of the longer one to longer - shorter. 
    p1 = 0
    p2 = 0
    res = []

    while p1 < len(encoded1) and p2 < len(encoded2):
        # Get the frequencies and products of the 2 arrays
        freq1 = encoded1[p1][1]
        freq2 = encoded2[p2][1]
        freq = min(freq1, freq2)
        product = encoded1[p1][0] * encoded2[p2][0]
        # Check if product exists as last val in res
        if res and product == res[-1][0]:
            # If so, update freq
            res[-1][1] += freq
        else:
            # Otherwise, add product, freq to result
            res.append([product, freq])
        # Move the pointers based on freq1 and freq2
        # If freq are equal, move both pointers.
        if freq1 == freq2:
            p1 += 1
            p2 += 1
        # Increment the smaller pointer (it's been used)
        # Decrement smaller from larger freq
        elif freq1 > freq2:
            #Increment smaller
            p2 += 1
            # Update freq of larger
            encoded1[p1][1] -= freq2
        else:
            p1 +=1
            encoded2[p2][1] -= freq1
    
    return res

encoded1 = [[1,3],[2,3]]
encoded2 = [[6,3],[3,3]]
print(findRLEArray(encoded1, encoded2))
encoded1 = [[1, 3], [2, 1], [3, 2]]
encoded2 = [[2, 3], [3, 3]]
print(findRLEArray(encoded1, encoded2))

# T: O(N) - go through both arrays once.
# S: O(N) - we have to keep the result

            
            
