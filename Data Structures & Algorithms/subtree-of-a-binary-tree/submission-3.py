# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 

        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        #be careful is putting subRoot. I mistakently put subRoot.left
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def sameTree(self, root, subRoot): # Added self, matched casing to subRoot
            # 1. Check if both are null
            if not root and not subRoot:
                return True 

            # 2. Check if only one of them is null
            if not root or not subRoot:
                return False

            # 3. Check if values match
            if root.val != subRoot.val:
                return False 

            # 4. Recursively check children (using matching variable casing)
            a = self.sameTree(root.left, subRoot.left)
            b = self.sameTree(root.right, subRoot.right)

            # 5. Clean explicit return
            return a and b

            