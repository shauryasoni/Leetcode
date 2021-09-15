# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rec(self,node,n1,n2):
        if node == None :
            return [False,False,None]
        else :
            props = [False,False,None]
            if node.val == n1 :
                props[0] = True
            if node.val == n2 :
                props[1] = True
                
            l = self.rec(node.left,n1,n2)
            if l[0:2] == [True,True] :
                return l
            
            r = self.rec(node.right,n1,n2)
            if r[0:2] == [True,True] :
                return r
            l[0] = l[0] or r[0]
            l[1] = l[1] or r[1]
            #print(node.val,l[0] or props[0],l[1] or props[1])
            if (l[0]or props[0])==True and (l[1] or props[1])== True :
                return [True,True,node]
            else :
                return [  (l[0]or props[0]) , (l[1] or props[1]) ,None  ]
            
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        return self.rec(root,p.val,q.val)[2]
        
