

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def iterative_inorderTraversal(self, root: TreeNode):
        
        stack = []
        result = []
        
        while root is not None or stack != []:
            
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        
        return result

    def recursive_inorderTraversal(self, root: TreeNode):
        
        
        if root is None:
            return []
        
        return self.recursive_inorderTraversal(root.left) + [root.val] + self.recursive_inorderTraversal(root.right)
    
    
    
    
    
    