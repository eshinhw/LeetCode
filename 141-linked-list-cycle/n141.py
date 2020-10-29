
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        # empty LL or a single LL (can't be a cycle)
        if head == None or head.next == None:
            return False
        
        curr = head
        
        while (curr != None):
            
            if curr.val != 'visited':
                curr.val = 'visited'
                curr = curr.next
            else:
                return True
        
