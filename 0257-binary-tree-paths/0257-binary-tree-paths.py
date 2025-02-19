# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.output = []        
        self.path = ""

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if (root):
            self.path += str(root.val) + "->"
            print(self.path)
            if root.left is None and root.right is None:                
                self.output.append(self.path[:-2])
            self.binaryTreePaths(root.left)
            self.binaryTreePaths(root.right)
            self.path = self.path[:-1*(len(str(root.val))+2)]
        return self.output
            
