class Solution:
    def hasPathSum(self,root, S):
        if root== None :
            return False
        if root.left == None and root.right == None :
            if S - root.data == 0 :
                return True
            else :
                return False
        else :
            return self.hasPathSum(root.left,S-root.data) or self.hasPathSum(root.right,S-root.data)