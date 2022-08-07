# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        return self.dfs(root,root)
        
    def dfs(self,node1,node2):
        if not node1 and not node2: return True
        if not node1 or not node2: return False
        
        return (node1.val == node2.val) and self.dfs(node1.right,node2.left) and self.dfs(node1.left,node2.right)
        