class Solution:
    # This problem is hard to understand and the description is meant to confuse. 
    # What we need to do is start at n = 1, which is the base case and the count.
    # Then for n = 2, we need to say the count, where it is One 1. This is represented as 11. 
    # Then for n = 3, we need to say 11, which would be two 1s. Which is represented as 21.
    # Then for n = 4, we need to say 21, which is One 2 and One 1. Which is represented as 1211. 
    # Then for n = 5, we need to say 1211, which is One 1, One 2, Two 1s, represented as 111221. 
    # Basically we can do this recursively. The base case is when n = 1, we just return 1. 
    # Then for all subsequent numbers, we call dfs(n - 1) to get the count.
    # Then we call our helper function to translate the count and say it. 
    # To translate, we go through the count and if we are in bounds and see that the next char is the same as current, we increment count.
    # Otherwise, we add the count and the digit to the result and reset the counter since the next digit will be different. 
    # We can return that from our dfs function. 
    def countAndSay(self, n: int) -> str: 

        # Translate the count
        def sayCount(count):
            result = []
            counter = 1
            for i in range(len(count)):
                # When we reach the end of a repetitive sequence
                if i == len(count) - 1 or count[i] != count[i + 1]:
                    result.append(str(counter))
                    result.append(str(count[i]))
                    # Reset the counter since we know this sequence has ended
                    counter = 1
                else:
                    counter += 1
            return ''.join(result)


        def dfs(i):
            if i == 1:
                return "1"
            # Call dfs(n - 1) to get the count
            count = dfs(i - 1)
            # Say the count
            return sayCount(count)
        
        return dfs(n)

# T: O(N * K), we have to call dfs n times and in each dfs, we have to traverse the count at that point in time (call that k).
# S: O(N) to account for the stack frames and the result array. 