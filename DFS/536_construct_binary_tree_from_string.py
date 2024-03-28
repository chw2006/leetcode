class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left is not None or root.right is not None:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

def str2tree(s):
    if not s:
        return None
    if len(s) == 1:
        return TreeNode(int(s[0]))
    # Use 1 stack to keep track of nodes we've encountered
    # Use another to keep track of the parentheses we encounter
    node_stack = []
    p_stack = []
    
    # Iterate through the string
    i = 0
    while i < len(s):
        c = s[i]
        # If we see an opening parentheses, add it to the stack
        if c == '(':
            p_stack.append(c)
        # If we see a closing parentheses, pop from both stacks
        elif c == ')':
            p_stack.pop()
            node_stack.pop()
        else:
            # Otherwise we have a number. Because a number may be larger than 1 char, we have to get the whole number
            num = 0
            # From i, iterate until we no longer see a digit
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            # Because we iterate using i, it will increment i 1 place farther than it needs to be, so decrement by 1
            i -= 1
            # Create a new node with the number as the value
            new_node = TreeNode(num)
            # If we know there is a parent node, set this to one of its children. 
            if node_stack:
                # Get the value at the top of the node stack
                parent_node = node_stack[-1]
                # If the node has no left child, set it as a left child. if it has a left child, set it as a right child
                if parent_node.left:
                    parent_node.right = new_node
                else:
                    parent_node.left = new_node
            # Add this to the node stack
            node_stack.append(new_node)
        i += 1
    
    # The stack should have 1 value left in the end, that is the root of the tree constructed
    return node_stack[-1]
                
s = "4(2(3)(1))(6(5))"
print_tree(str2tree(s))
s = "1(2(3)(4))(5)"
print_tree(str2tree(s))

# Time Complexity: O(N), we go through the string once
# Space Complexity: O(N), since this is iterative, we don't need to account for recurisve stack frames. But we do use 2 stacks. However, neither have more than N items on them since they are all just part of the string. 



