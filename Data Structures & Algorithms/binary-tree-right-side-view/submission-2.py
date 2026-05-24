# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #what we can do is run the dfs and return the last integer from the each level. 

        value = []
        q = deque()
        if root:
            q.append(root)

        while q: 
            rightSide = None
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide: 
                value.append(rightSide.val)
        return value

            
        


        