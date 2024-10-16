# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        r1, r2 = [], []

        def traverse(p):
            if p is None:
                r1.append(None)
                return
            r1.append(p.val)
            traverse(p.left)
            traverse(p.right)
        
        def traverse2(q):
            if q is None:
                r2.append(None)
                return
            r2.append(q.val)
            traverse2(q.left)
            traverse2(q.right)
        
        traverse(p)
        traverse2(q)

        if r1 == r2:
            return True
        return False