from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        answer = root

        def dfs(root):
            if root is None:
                return
            tmp = root.left
            root.left = root.right
            root.right = tmp
            dfs(root.right)
            dfs(root.left)
        dfs(root)

        return answer