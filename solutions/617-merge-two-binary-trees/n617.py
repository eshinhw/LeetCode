

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        return self.merge(t1, t2)
    
       
    def merge(self, t1, t2):
        
        if t1 == None and t2 == None:
            return None
        
        if t1 == None and t2 != None:
            return t2
        
        if t1 != None and t2 == None:
            return t1
        
        out = TreeNode(t1.val + t2.val)
        
        out.left = self.merge(t1.left, t2.left)
        
        out.right = self.merge(t1.right, t2.right)
        
        return out
        
        
        
        