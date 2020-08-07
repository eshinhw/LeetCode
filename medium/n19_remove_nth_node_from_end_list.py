# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Concept of slow and fast pointer
"""

class Solution:
    def removeNthFromEnd(self, head, n):
        
        dummy = ListNode(-1)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        for i in range(n+1):
            slow = slow.next
        
        while fast != None:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        
        return dummy.next
        
        