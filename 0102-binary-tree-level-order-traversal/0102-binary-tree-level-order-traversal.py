# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right        

class Solution:
    def __init__(self):
        self.arr = []
        self.height = 1
        self.max_height = 1        
    
    def f_height(self, root):
        if (root):            
            if self.height > self.max_height:
                self.max_height = self.height
            self.height += 1
            self.f_height(root.left)   
            self.f_height(root.right)
            self.height -= 1
    
    def f_arr(self):        
        self.arr = [[] for _ in range(self.max_height)]
    
    def f_answer(self, root):        
        if (root):                 
            self.arr[self.height-1].append(root.val)
            self.height += 1
            self.f_answer(root.left)   
            self.f_answer(root.right)
            self.height -= 1

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.f_height(root)
        self.f_arr()        
        self.f_answer(root)
        
        if self.arr[0] == []:
            self.arr = []
        return self.arr
        
