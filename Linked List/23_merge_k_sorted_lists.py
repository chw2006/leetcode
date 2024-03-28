# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # We want to merge the lists in pairs. This cuts down our runtime to O(nlogk)
        # Have a check to see if the 2nd pair of lists exists. 
        # Helper function to help merge the 2 lists together
        def mergeLists(list1, list2):
            # Use a dummy node to make this easier
            dummy = ListNode()
            curr = dummy

            # Merge the 2 lists
            while list1 and list2:
                # If list2 is larger, list1 comes first
                if list2.val > list1.val:
                    curr.next = list1
                    list1 = list1.next
                # If list1 is larger, list2 comes first
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            # If either list1 or list2 has extras, put them at the end
            if list1:
                curr.next = list1
            
            if list2:
                curr.next = list2

            return dummy.next 
        
        if not lists or len(lists) == 0:
            return None

        # We want to merge until lists only has one list in it
        while len(lists) > 1:
            # Keep track of the lists that were merged
            merged = []
            # We want to merge in pairs, so increment by 2
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = None
                # Check that i + 1 is in bounds
                if (i + 1) < len(lists):
                    l2 = lists[i + 1]
                # Call the helper to merge the lists
                merged.append(mergeLists(l1, l2))
            # Update lists to merged
            lists = merged

        return lists[0]