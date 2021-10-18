
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rec(self, node,t,s,visited) :
        if s == None and node in visited:
            return 0
        
        if node == None :
            return 0
        
        else :
            if s == None :
                visited.add(node)
                s = node.val
            else :
                s = s + node.val
            
            l,r = 0,0
            if node.left :
                l = self.rec(node.left,t, None,visited)
            if node.right :
                r = self.rec(node.right,t, None,visited)
            c = self.rec(node.left,t,s,visited) + self.rec(node.right,t,s,visited)
            if s == t :
                print(node.val)
                return 1 + l + r + c
            return l + r + c
                
            
    def pathSum(self, root:TreeNode, targetSum: int) -> int:
        visited = set()
        return self.rec(root, targetSum,None,visited)