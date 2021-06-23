# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Concept of slow and fast pointer
"""

class Solution:
    
    def removeNthFromEndv1(self, head, n):
        
        # Count the length of input linked list
        
        curr = head
        length = 0
        while (curr != None):
            length += 1
            curr = curr.next
        
        # Subtract the given n from the length
        
        loc = length - n
        
        curr = head
        prev = None
        
        while (loc != 0):
            
            loc -= 1
            prev = curr
            curr = curr.next
            
        # Remove a node
        
        if prev == None:
            return head.next
        else:
            prev.next = curr.next
            curr.next = None      
            return head       
        
    
    def removeNthFromEndv2(self, head, n):
        
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
        
        
