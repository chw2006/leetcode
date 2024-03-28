class Solution:
    def myPow(self, x: float, n: int) -> float:
        # We know that 2**n = 2**n/2 * 2**n/2. 
        # So we can make this logn time by doing divide and conquer. 
        # If n is even, it's trivial. Just divide n by 2 every time and keep multiplying the result by itself. 
        # If n is odd, we have to also multiply the result by x. 
        # If n is negative, we have to return 1 / result. 
        def power(x, n):
            # Base cases
            if x == 0:
                return 0
            # Anything to the 0th power is 1
            if n == 0:
                return 1
            # Divide n by 2 and recursively call power
            res = power(x, n // 2)
            # Multiply res by itself 
            res *= res
            # If n is odd, we have to multiply res by x, otherwise return res
            if n % 2:
                return res * x
            else:
                return res

        res = power(x, abs(n))

        # If n is less than 0, we want 1 / result.
        if n >= 0:
            return res
        else:
            return 1 / res

# Time Complexity: O(logN): Because we're doing divide and conquer by dividing n by 2 every time, it's O(logN). 
# Space Complexity: O(N): We're using recursion, so we have to account for stack frames. 