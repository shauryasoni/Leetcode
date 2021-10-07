class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        if root == None :
            return 0
        else :
            left = 1 + self.height(root.left)
            right = 1 + self.height(root.right)
            return max(left,right)