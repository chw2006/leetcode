class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # Use a stack to keep track of the execution stack. 
        # We need to keep track of the previous start time using prev_time. 
        stack = []
        result = [0] * n
        prev_time = 0

        for i in range(len(logs)):
            # Go through the logs and parse out the id, time, and operation. 
            cur = logs[i].split(":")
            cur_id = int(cur[0])
            cur_time = int(cur[2])
            cur_op = cur[1]
            # For starting points, we push the id to the stack. 
            # We also must account for any previous running functions.
            if cur_op == "start":
                # If there is a previous running function, update that function's time. 
                if stack:
                    prev_id = stack[-1]
                    result[prev_id] += cur_time - prev_time
                # Add this id to the stack and update the prev_time to the current time. 
                stack.append(cur_id)
                prev_time = cur_time
            # For ending points, we pop from the stack
            elif cur_op == "end":
                prev_id = stack.pop()
                # The time here is inclusive, so we must add a 1
                result[cur_id] += cur_time + 1 - prev_time
                # Because the time is inclusive, the prev_time must also be updated with a + 1. 
                prev_time = cur_time + 1
        return result

#T: O(N)
#S: O(N), we use a stack and keep track of the result. 