"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def bfs(self,frontier) :
        if frontier == [] :
            return 
        else :
            level = []
            for i in frontier :
                if i.left :
                    level.append(i.left)
                if i.right :
                    level.append(i.right)
            if level== [] :
                return
            else :
                for i in range(len(level)) :
                    if i!=len(level)-1 :
                        level[i].next = level[i+1]
                    else :
                        level[i].next = None
            self.bfs(level)
            
        
    def connect(self, root: 'Node') -> 'Node':
        if root == None :
            return None
        root.next == None
        frontier = [root]
        
        self.bfs(frontier)
        return root
