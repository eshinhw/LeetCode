
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        count = 0
        nodes = []
        
        curr = head
        
        while (curr != None):
            count += 1
            nodes.append(curr)
            curr = curr.next
        
        if count == 1:
            return head
        
        if count == 2:
            return head.next
        
        return nodes[count // 2]


        