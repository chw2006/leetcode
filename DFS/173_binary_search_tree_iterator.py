# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    # We will use iterative DFS inorder traversal to traverse this tree.
    # In the constructor traverse all the way down to the first leaf node to make it easier when we call hasNext()
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.curr = root

        # Iterate all the way to the leaf node (first value we will print)
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left

    def next(self) -> int:
        # Print the next value
        # For example, if we are at our first leaf node, curr will be None
        # We then pop from the stack, get its value, set curr to the right child and return the value. 
        # If we were at a non-leaf node, we would keep exploring left and adding nodes to the stack until we can return the next value. 
        while self.curr or self.stack:
            if self.curr:
                self.stack.append(self.curr)
                self.curr = self.curr.left
            else:
                self.curr = self.stack.pop()
                value = self.curr.val
                self.curr = self.curr.right
                return value

    def hasNext(self) -> bool:
        # We know there is a next value if we have a value on the stack or if curr exists. 
        if self.curr or self.stack:
            return True
        else:
            return False

# Time Complexity: O(N)
# Space Complexity: O(N) need to use a stack to hold all N nodes. 

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()