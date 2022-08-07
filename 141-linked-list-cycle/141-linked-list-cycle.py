# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head      
        visited = {}
        
        while node:
            if node in visited:
                return True
            
            visited[node] = True
            
            node = node.next
            
        return False
                
    def hasCycleFloyd(self, head:ListNode) -> bool:
        if head is None:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            
        return True