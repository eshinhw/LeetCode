
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head == None:
            return True
        if head.next == None:
            return True
        
        valueList = []
        
        current = head
        
        while (current != None):
            valueList.append(current.val)
            current = current.next
        
        start = 0
        end = len(valueList) - 1
        
        while (start < end):
            
            if valueList[start] == valueList[end]:
                start += 1
                end -= 1
            else:
                return False
        
        return True
    
    
    