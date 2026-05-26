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
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        #in here we need to convert the string into the data.
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "NaN":
                self.i +=1
                return None 

            node = TreeNode(int(vals[self.i]))
            self.i +=1
            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


