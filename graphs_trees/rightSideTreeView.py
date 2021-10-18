
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
from typing import List
class Solution:
    def bfs(self,ans,frontier):
        if frontier == [] :
            return
        
        level = []
        for i in frontier :
            if i.left !=None :
                level.append(i.left)
            if i.right != None :
                level.append(i.right)
        if level == []:
            return
        
        ans.append(level[-1].val)
        self.bfs(ans,level)
            
        
        
        
    def rightSideView(self, root:TreeNode) -> List[int]:
        if root == None :
            return []
        
        ans = [root.val]
        self.bfs(ans,[root])
        return ans
#This code does bfs and returns the last element in every level. It returns the right side view