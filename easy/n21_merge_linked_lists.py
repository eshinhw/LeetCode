"""
21. Merge Two Sorted Lists
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1:
            return l2
        
        if not l2:
            return l1        
        
        dummy = ListNode(-1)
        curr = dummy
        
        curr1 = l1
        curr2 = l2
        
        while (curr1 != None or curr2 != None):
            
            if curr1 is None and curr2 is not None:                
                curr.next = curr2
                break                
                
            if curr1 is not None and curr2 is None:                
                curr.next = curr1
                break
            
            if curr1.val < curr2.val:                
                curr.next = ListNode(curr1.val)
                curr1 = curr1.next
                curr = curr.next

            else:
                curr.next = ListNode(curr2.val)
                curr2 = curr2.next
                curr = curr.next
            
        return dummy.next