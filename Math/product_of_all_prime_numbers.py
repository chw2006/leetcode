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

primes = [2, 3, 11]
print(productOfAllPrimes(primes))

