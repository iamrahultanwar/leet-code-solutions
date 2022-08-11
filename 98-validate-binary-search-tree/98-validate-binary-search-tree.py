# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.dfs(root,float("-inf"),float("inf"))
        
        
    def dfs(self,node,left,right):    
        if node is None:
            return True
        if not (node.val < right and node.val > left):
            return False
        return self.dfs(node.left,left,node.val) and self.dfs(node.right,node.val,right)
    
    
        
        
        