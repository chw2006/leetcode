def findRLEArray(encoded1, encoded2):
    # Doing it the way the problem describes it is way too inefficent, there is a 2 pointer solution
    # That can achieve this in one pass. 
    # Go through both arrays at the same time.
    # If the frequency is the same, multiply the values and add to result. Increment i and j. 
    # If the frequencies are not the same, take the min of the 2.
    # Increment the pointer of the smaller frequency. 
    # Set the frequency of the longer one to longer - shorter. 
    
    i = 0
    j = 0
    res = []
    # Finds the index of the array with the input product
    def find_product(product):
        for i in range(len(res)):
            if res[i][0] == product:
                return i
        return -1

    while i < len(encoded1) and j < len(encoded2):
        product = encoded1[i][0] * encoded2[j][0]
        # If this value already exists in the result, add to it, do not put in a new entry
        product_index = find_product(product)
        # If the product is in the result, add ot it
        if product_index >= 0:
            # We are adding to the frequency of the product index we found
            res[product_index][1] += min(encoded1[i][1], encoded2[j][1])
        else:
            # Otherwise, just add it to the result
            res.append([product, min(encoded1[i][1], encoded2[j][1])])

        # Increment both if the freq is equal
        if encoded1[i][1] == encoded2[j][1]:
            i += 1
            j += 1
        # Increment the pointer of the smaller frequency and update the frequency of the larger
        elif encoded1[i][1] < encoded2[j][1]:
            encoded2[j][1] -= encoded1[i][1]
            i += 1
        else:
            encoded1[i][1] -= encoded2[j][1]
            j += 1
        
    return res

encoded1 = [[1,3],[2,3]]
encoded2 = [[6,3],[3,3]]
print(findRLEArray(encoded1, encoded2))


            
            
