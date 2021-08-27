# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution :
    def maxtheft(self,node,d) :
        if node==None :
            return 0
        elif node in d :
            return d[node]
        else :
            if node.left==None and node.right!=None:
                d[node] =  max((node.val+self.maxtheft(node.right.left,d)+self.maxtheft(node.right.right,d)),self.maxtheft(node.right,d))
                return d[node]
            elif  node.left!=None and node.right==None:
                d[node] =  max((node.val+self.maxtheft(node.left.left,d)+self.maxtheft(node.left.right,d)),self.maxtheft(node.left,d))
                return d[node]
           
            elif node.left == None and node.right == None :
                d[node] = node.val
                return d[node]
           
            else :
                d[node] = max((node.val + self.maxtheft(node.left.left,d) + self.maxtheft(node.left.right,d) +                   self.maxtheft(node.right.right,d)+self.maxtheft(node.right.left,d))  ,(self.maxtheft(node.left,d) + self.maxtheft(node.right,d)))
                return d[node]
    def rob(self, root) -> int:
        d = {}
        val = self.maxtheft(root,d)
        #print(type(root))
        return(val)

print(Solution.rob([1,2,3,4,None,None,5,6,None,None,None]))
#Pass in the root of the tree. Code works
