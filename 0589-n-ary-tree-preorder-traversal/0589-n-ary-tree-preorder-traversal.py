
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def __init__(self):
        self.li = []

    def preorder(self, root: 'Node') -> List[int]:
        if (root):
            self.li.append(root.val)
            for child in root.children:
                self.preorder(child)
        return self.li