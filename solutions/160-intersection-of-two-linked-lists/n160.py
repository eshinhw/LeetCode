
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        p1 = headA
        p2 = headB
        
        while (p1 != p2):
            
            if p1 == None:
                p1 = headB
            else:
                p1 = p1.next
                
            if p2 == None:
                p2 = headA
            else:
                p2 = p2.next
        
        return p2           


    def _getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        
        savedA, savedB = headA, headB
        
        while headA != headB:
            headA = savedB if not headA else headA.next
            headB= savedA if not headB else headB.next
            
        return headA
    
    
    