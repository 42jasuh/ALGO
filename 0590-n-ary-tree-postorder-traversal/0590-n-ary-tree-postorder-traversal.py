
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.li = []
    
    def p_order(self, root: 'Node') -> List[int]:
        if (root):
            for child in root.children:
                self.p_order(child)
                self.li.append(child.val)        
        return self.li
    
    def helper(self, root: 'Node') -> List[int]:        
        res = self.p_order(root)
        if (root):
            res.append(root.val)
        return res

    def postorder(self, root: 'Node') -> List[int]:
        return self.helper(root)
        