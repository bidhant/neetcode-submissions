# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # we need to do recursiro for both the left and the right and while we are doing this we need to check if they have the same value, and whether they have nodes or not. 
        if not p and not q:
            return True 

        if (p and not q) or (not p and q): 
            return False 

        if p.val != q.val:
            return False 

        a = self.isSameTree(p.left, q.left)
        b = self.isSameTree(p.right, q.right)

        return a and b

        

