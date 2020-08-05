

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        values = []
        
        curr = head
        
        while (curr != None):
            values.append(curr.val)
            curr = curr.next
        
        first = 0
        last = len(values) - 1
        
        while (first < last):
            
            if values[first] != values[last]:
                return False
            else:
                first += 1
                last -= 1
        
        return True