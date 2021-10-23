class Solution:
    def toSumTree(self, root) :
        #code here
        if root == None :
            return 0
        if root.left == None and root.right == None :
            temp = root.data
            root.data = 0
            return temp
        else :
            left = self.toSumTree(root.left)
            right = self.toSumTree(root.right)
            temp = root.data
            root.data = left + right
            return left + right + temp