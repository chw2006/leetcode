# To get all the possible products of a list of primes, we start off with the base case.
# Which is that if the prime list is empty, we just return 1. 
# Then we go through the primes and multiply the prime with the previous result. 
# Because we are looping through result, we have to create a copy of it and add the results there. 
# We set res to tmp for every prime value.
def productOfAllPrimes(primes):
    res = [1]
    # Go through all primes in the array
    for prime in primes:
        # Copy the current results into tmp so we don't modify the array we loop though
        tmp = res.copy()
        for r in res:
            # Append the results * each prime to tmp
            tmp.append(r * prime)
        # Set res to tmp
        res = tmp
    return res
# T: O(N^2) - have to loop through primes and its previous products. 
# S: O(N^2) - We have to copy res for each prime value, along with storing it. So O(N^2)
primes = [2, 3, 11]
print(productOfAllPrimes(primes))

# Solution using recursion
# Go through the primes array and do a dfs of sorts.
# When we are at the end of the string, add the current product, this is the base case.
# We can either include the prime value or not include the prime value.
# If we include it, we have to multiply the current product, otherwise, we just increment the index and keep the same product.
def recursivePrimeProducts(primes):
    res = []
    def dfs(i, product):
        if i == len(primes):
            res.append(product)
            return
        # Either include or not include this
        # Include
        dfs(i + 1, product * primes[i])
        # Don't include
        dfs(i + 1, product)

    dfs(0, 1)
    return res

# T: O(2^N) - have to make 2 recursive calls.
# S: O(2^N) - have to store all solutions in a list. If there are 2^N solutions, we gotta store them all. 

primes = [2, 3, 5, 7]
print(recursivePrimeProducts(primes))
