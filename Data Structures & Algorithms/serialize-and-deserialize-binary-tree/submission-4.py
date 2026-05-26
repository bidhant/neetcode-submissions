# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        #this one is to convert it into string 
        result = []
        def dfs(root):
            if not root:
                result.append("NaN")
                return None
            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

            return result

        dfs(root)
        return ",".join(result)

    # [1,2,n,n,3,4,n,n,5,n,n]
        
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Convert the split list into a double-ended queue
        queue = deque(data.split(","))

        def dfs():
            # Pop the first element from the front of the queue
            val = queue.popleft()
            
            if val == "NaN":
                return None

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            
            return node

        return dfs()


