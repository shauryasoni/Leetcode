class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rec(self,node) :
        if node == None :
            return None 
        else :
            
            left = self.rec(node.left)
            
            right = self.rec(node.right)
            curr = left
            
            while curr and curr.right!=None :
                curr = curr.right
            
            if right == None :
                node.left = None
                node.right = left
            else :
                if curr == None :
                    pass
                else :
                    curr.right = right
                    node.right = left
                    node.left = None

            return node
            
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None :
            return None
        if root.left == None and root.right == None :
            return root
        self.rec(root)