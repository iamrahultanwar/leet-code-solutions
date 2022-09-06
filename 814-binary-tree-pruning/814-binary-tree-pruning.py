# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        
        def bfs(node):           
            if node is None:
                return True # remove, val
            
            leftSide = bfs(node.left)
            rightSide = bfs(node.right)
            
            if leftSide:
                node.left = None
                
            if rightSide:
                node.right = None
            
            remove = leftSide and rightSide and node.val == 0
            
            
            return remove
            
            
        bfs(root)
        
        if root.left is None and root.right is None and root.val == 0:
            root = None
            
        return root
            
            
            
        