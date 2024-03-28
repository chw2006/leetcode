class Solution:
    # Base case is if we hit the end of the string and the result is the same as our target. Add that value to the result.
    # For the dfs function, we need to keep track of the current result, sum, the index, the previous number.
    # When parsing the string, we can either parse one char or parse multiple chars until the end of the string.
    # After that, there are 3 different possibilities. 
    # We can choose to add the current digit, we can choose to subtract the current digit, and we can choose to multiply the current digit. 
    # Multipication has a different order of operations, so we must subtract the previous value, then add the prev value * current value.
    # Because we cannot account for leading 0s (such as 03), when we see a 0 and the current string is larger than length 1, we need to break out of that. 
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []

        def dfs(idx, curr_res, curr_sum, prev):
            # Base case
            if idx >= len(num):
                # If sum is equal to target, add this to the result
                if curr_sum == target:
                    res.append("".join(curr_res))
                return

            # We can parse the number anyway we like (except leading 0s)
            for i in range(idx, len(num)):
                # Get the current string and num
                curr_str = num[idx: i + 1]
                curr_num = int(curr_str)
                # Edge case for first value in string
                if not curr_res:
                    dfs(i + 1, [curr_str], curr_num, curr_num)
                else:
                    # 3 possible different cases
                    # Addition
                    dfs(i + 1, curr_res + ["+"] + [curr_str], curr_sum + curr_num, curr_num)
                    # Subtraction
                    dfs(i + 1, curr_res + ["-"] + [curr_str], curr_sum - curr_num, -curr_num)
                    # Multiplication
                    # To get the sum, we have to subtract previous then add prev * curr
                    dfs(i + 1, curr_res + ["*"] + [curr_str], curr_sum - prev + (prev * curr_num), prev * curr_num)
                
                # Because we cannot have a leading 0 value. One single 0 is ok, but anything more than length of 1 is not.
                # So we let single 0s go through the process, but once it's longer than 1 char, we break. 
                if num[idx] == '0':
                    break

        dfs(0, [], 0, 0)

        return res

# Time Complexity: 4^N * N, because there are 4 branches (don't include this char, add, subtract, multiply) and we have to join the array for each solution. 
# Space Complexity: O(N), we store the results in an array. 