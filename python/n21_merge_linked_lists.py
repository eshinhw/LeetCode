
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        while l1.next != None and l2.next != None:
            
            cur1 = l1.val
            cur2 = l2.val
            
            if cur1 == cur2:
                temp = l1.next
                l1.next = l2
                l2.next = temp
            
            
        