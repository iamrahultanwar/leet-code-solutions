# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
            maxLength = [0]
            def dfs(node,parent,length):
                if node is None:
                    return
                
                length = length + 1 if parent is not None and node.val == parent.val + 1 else 1
                
                maxLength[0] = max(maxLength[0],length)
                
                dfs(node.left,node,length)
                dfs(node.right,node,length)

                
            dfs(root,None,0)

            return maxLength[0]