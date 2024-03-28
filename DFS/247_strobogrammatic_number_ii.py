def findStrobogrammatic(n):
    # This is a recursive problem
    # We know that for n = 0, we should return an empty list.
    # When n = 1, we know that the strobogrammatic numbers are 0, 1, and 8. These are the base cases.
    # For all other n values, they take the values at n - 2 and use them as a base. 
    # They then add a pair of values surrounding the base. The values are (1, 1), (6, 9), (8, 8), and (9, 6)
    # Once we take every base value from n - 2 and surround them with the above pairs, we will get the values for that n. 
    pairs = [('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
    def dfs(i):
        if i == 0:
            return ['']
        if i == 1:
            return ['0', '1', '8']
        
        base = dfs(i - 2)
        res = []
        
        # Go through every base and add the pairs around the base
        for b in base:
            for l, r in pairs:
                res.append(l + b + r)
            if i != n:
                # We can add 0 as a pair as well if we are not at n
                res.append('0' + b + '0')
        return res

    return dfs(n)

res = findStrobogrammatic(4)
print(res)

# T: O(5^(N / 2)): There are 5 digits to choose from for every N. However, because we do a recursive call to n - 2, it halves the work. 
# S: O(5^(N / 2)): Space complexity is proportional to the number of combinations. Stack storage would be O(N), which compared to O(5&(N/2)) does not matter. 