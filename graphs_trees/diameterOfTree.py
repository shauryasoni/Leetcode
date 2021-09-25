# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) :
        self.max = 0
        
    def rec(self,node)     :
        if node == None :
            return 0
        else :
            left = 1 + self.rec(node.left)
            right = 1 + self.rec(node.right)
            mpath = left + right -2
            if mpath > self.max :
                self.max = mpath 
            return max(left,right)
    
    
    def diameterOfBinaryTree(self, root) -> int:
        self.rec(root)
        return self.max