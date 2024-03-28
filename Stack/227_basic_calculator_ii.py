class Solution:
    def calculate(self, s: str) -> int:

        def stack():
            stack = []
            result = 0
            cur = 0
            op = "+"
            i = 0

            while i < len(s):
                c = s[i]
                if c.isdigit():
                    # Change the string into an int
                    while i < len(s) and s[i].isdigit():
                        cur = cur * 10 + int(s[i])
                        i += 1
                    # This offsets the later i increment
                    i -= 1
                    # For add and subtract, we simply add/subtract to the stack
                    if op == "+":
                        stack.append(cur)
                    elif op == "-":
                        stack.append(-cur)
                    # For multiplicationa and division, we have to pop from the stack and then append the new multiplied/divide value
                    elif op == "*":
                        top = stack.pop()
                        stack.append(cur * top)
                    else:
                        top = stack.pop()
                        stack.append(int(top / cur))
                    cur = 0
                # If it's a non whitespace and non-digit char, it's an operator
                elif c != ' ':
                    op = c
                i += 1
            
            # Sum up the values in the stack
            while stack:
                result += stack.pop()

            return result
        
        return stack()
                    

        def non_stack():
            cur = 0
            prev = 0
            result = 0
            op = "+"
            i = 0

            while i < len(s):
                c = s[i]
                # If the character is a digit, then we can process it
                if c.isdigit():
                    # For numbers with more than a single digit, we have to turn it into an integer.
                    while i < len(s) and s[i].isdigit():
                        cur = cur * 10 + int(s[i])
                        i += 1
                    # This negates the i increment later on
                    i -= 1
                    # If we add, we add the current to the result. Set current as prev
                    if op == "+":
                        result += cur
                        prev = cur
                    elif op == "-":
                        result -= cur
                        prev = -cur
                    elif op == "*":
                        # Undo the previous operation
                        result -= prev
                        # Add prev * cur to the result
                        result += prev * cur
                        # Prev is prev * current
                        prev = prev * cur
                    else:
                        # For division
                        result -= prev
                        result += int(prev / cur)
                        prev = int(prev / cur)
                    # Reset cur
                    cur = 0
                elif c != ' ':
                    op = c
                
                i += 1
            
            return result