
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList_iter(self, head: ListNode) -> ListNode:

        prev = None
        curr = head
        nxt = None

        while (curr != None):

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head = prev

        return head

    def reverseList_recur(self, head: ListNode) -> ListNode:

        # If head is empty or has reached the list end
        if head is None or head.next is None:
            return head

        # Reverse the rest list
        rest = self.reverse(head.next)

        # Put first element at the end
        head.next.next = head
        head.next = None

        # Fix the header pointer
        return rest