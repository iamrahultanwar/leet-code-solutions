# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result=[root.val]
        
        
        def dfs(node):
            
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            left = max(left,0)
            right = max(right,0)
            
            result[0] = max(result[0],left+right+node.val)
            
            return node.val + max(left,right)
        
        
        dfs(root)
        
        return result[0]