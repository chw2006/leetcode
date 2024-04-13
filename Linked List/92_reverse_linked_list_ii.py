# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Use a dummy node and set its next to previous.
    # Iterate left - 1 times so that previous points to the node previous to left and curr points to left.
    # Reverse the list from left to right + 1. To reverse list, save curr.next to nxt. Set curr.next to previous. Set curr to nxt. 
    # After reversing the middle of the list, left_prev points to the node before the left node.
    # curr points to the node after right. prev points at right. 
    # So set left_prev.next.next to curr (after right)
    # Set left_prev.next to prev (right)
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        for _ in range(left - 1):
            prev = curr
            curr = curr.next
        
        left_prev = prev
        prev = None

        for _ in range(right - left  + 1):
            # Save curr to temp var
            nxt = curr.next
            # Reverse curr's next pointer to prev
            curr.next = prev
            # Set prev to curr
            prev = curr
            # Set curr to the temp next (original next)
            curr = nxt
        
        # left_prev points to the node before left. It is still linked to left node.
        # We can use its reference to the left to point its next to current (node after right)
        # We can use left_prev.next to point to right, since that is now the first node in the reversed list.
        left_prev.next.next = curr
        left_prev.next = prev

        return dummy.next

# T: O(N) - must traverse entire linked list in the worst case
# S: O(1)