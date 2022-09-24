# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        result = []
        
        def dfs(node,remainingSum,curr=[]):
            
            if node is None:
                return
            
            curr.append(node.val)
            
            if remainingSum == node.val and not node.left and not node.right:
                result.append(curr[::])
                
            else:
                dfs(node.left,remainingSum - node.val,curr)
                dfs(node.right,remainingSum - node.val,curr)
                
            
            curr.pop()
            
            
        dfs(root,targetSum,[])
        
        return result