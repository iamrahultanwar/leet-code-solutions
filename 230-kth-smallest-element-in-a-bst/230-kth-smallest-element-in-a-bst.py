# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        while stack or curr:
            
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()            
            
            k -= 1
            
            if k == 0:
                return curr.val
            
            curr = curr.right
            
            
            
    
    
        # visited = []   
        # self.dfs(root,visited)
        # return visited[k-1]
        
    
    def dfs(self,node,visited):
        
        if node is not None:
            
            self.dfs(node.left,visited)
            visited.append(node.val)
            self.dfs(node.right,visited)
            
        
            