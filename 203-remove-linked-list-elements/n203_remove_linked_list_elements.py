# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return None
        
        if (head.val == val) and (head.next == None):
            return None
        
        if (head.val != val) and (head.next == None):
            return head
        
        dummy = ListNode(-1)
        curr = dummy
        
        while (head != None):
            
            if head.val != val:
                curr.next = ListNode(head.val)
                curr = curr.next
                head = head.next
            else:
                head = head.next
        
        return dummy.next
    

    def removeElementsV2(self, head: ListNode, val: int) -> ListNode:
        
        dummy = ListNode(-1)
        dummy.next = head
        
        prev, curr = dummy, head
        
        while (curr != None):
            
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
        
        return dummy.next

