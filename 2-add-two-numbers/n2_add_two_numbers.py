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

        carry = 0

        while (t1 != None or t2 != None):

            digit_sum = t1.val + t2.val

            if (digit_sum >= 10):
                carry += 1
                remainder = digit_sum - 10
                output.next = ListNode(remainder)
            else:
                output.next = ListNode(digit_sum)




