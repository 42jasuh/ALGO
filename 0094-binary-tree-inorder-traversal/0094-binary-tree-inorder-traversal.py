# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root, arr):
        if not root:
            return
        self.helper(root.left, arr)
        arr.append(root.val)
        self.helper(root.right, arr)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.helper(root, arr)
        return arr