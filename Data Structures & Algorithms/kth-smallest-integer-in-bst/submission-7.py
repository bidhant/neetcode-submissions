# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #let me try this by myself 
        self.counter = 0
        self.result = 0
        def dfs(root):
            if not root:
                return None 

            dfs(root.left)
            
            self.counter +=1
            if self.counter == k:
                self.result = root.val
                return self.result

            dfs(root.right)
        
        dfs(root)
        return self.result


