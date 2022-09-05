# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def bfs(node):          
            if node is None:
                return
            
            temp = node.right
            node.right = node.left
            node.left = temp
            
            bfs(node.left)
            bfs(node.right)
            
            
        bfs(root)
        
        return root
            
            