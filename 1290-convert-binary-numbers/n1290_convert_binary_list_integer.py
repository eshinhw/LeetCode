
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        values = []
        
        curr = head
        
        while (curr != None):
            
            values.insert(0, curr.val)
            curr = curr.next
            
        
        total = 0
        power = 0
        
        for i in range(len(values)):
            if values[i] == 0:
                power += 1
            else:
                total = total + (values[i] * (2**power))
                power += 1
        
        return total
    
    
    