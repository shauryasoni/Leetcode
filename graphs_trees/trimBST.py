class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rec(self,root,high,low) :
        if root == None :
            return None
        else :
            if root.val >= low and root.val <= high :
                    root.left = self.trimBST(root.left,low,high)
                    root.right = self.trimBST(root.right,low,high)
                    #print(root)
                    
            elif root.val < low :
                #root.left = None
                root = root.right
                if root and root.val >= low and root.val <= high :
                    root.left = self.trimBST(root.left,low,high)
                    root.right = self.trimBST(root.right,low,high)
                else:
                    root = self.trimBST(root,high,low)
            else :
                #root.right = None 
                root = root.left
                if root and root.val >= low and root.val <= high :
                    root.left = self.trimBST(root.left,low,high)
                    root.right = self.trimBST(root.right,low,high)
                else :
                    root = self.trimBST(root,high,low)
                
            #print(root)   
            return root
    def trimBST(self, root: TreeNode, low: int, high: int) :
        
            
            return self.rec(root,high,low)