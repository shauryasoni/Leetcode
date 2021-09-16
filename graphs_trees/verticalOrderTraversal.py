from typing import List
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def vt(self,node,hd,d) :
        if node == None :
            return
        else :
            if hd in d :
                d[hd].append(node.val)
                d[hd] = sorted(d[hd])
            else :
                d[hd]= [node.val]
            self.vt(node.left,hd-1,d)
            self.vt(node.right,hd+1,d)
            
    def verticalTraversal(self, root) -> List[List[int]]:
        d = {}
        self.vt(root, 0, d)
        return [d[k] for k in sorted(d)]

#BELOW CODE IS ACCEPTED IN LEETCODE
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def vt(self,node,hd,level,d) :
        if node == None :
            return
        else :
            if hd in d :
                if level in d[hd] :
                    d[hd][level].append(node.val)
                    d[hd][level] = sorted(d[hd][level])
                else :
                    d[hd][level] = [node.val]
                
            else :
                d[hd]= {level : [node.val]}
                
            self.vt(node.left,hd-1,level + 1,d)
            self.vt(node.right,hd+1,level + 1,d)
            return
            
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = {}
        self.vt(root, 0,0, d)
        res = []
        for i in sorted(d) :
            k = []
            for j in sorted(d[i]):
                k.extend(d[i][j])
            res.append(k)
        return res
'''
            
            