# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        if l1 is None and l2 is None:
            return None


        output = ListNode(-1)

        t1 = l1
        t2 = l2

        while (t1 != None or t2 != None):



            output.next = ListNode(t1.val + t2.val)


