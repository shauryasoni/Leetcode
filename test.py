import collections
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        
        print("here")
        res = collections.deque([root.data])
        exl  = 0
        exr = 0
        level = 0
        frontier = collections.deque([root])
        
        allnone = False
        while allnone == False:
            print(res)
            level = level + 1
            lnodes = 2**level
            allnone = True
            for i in range(len(frontier)) :
                node = frontier.popleft()
                if node == None :
                    frontier.append(None)
                    frontier.append(None)
                    continue
                else :
                    
                    frontier.append(node.left)
                    frontier.append(node.right)
                
                if  node.left!= None or node.right!=None :
                    allnone = False
            middle = lnodes // 2
            for i in range(middle-1,-1,-1) :
                if i>= middle-exl :
                    continue
                else :
                    if frontier[i]!= None :
                        res.appendleft(frontier[i].data)
                        exl+=1
            for i in range(middle,len(frontier)) :
                if i<= middle + exr -1 :
                    continue
                else :
                    if frontier[i]!= None :
                        res.append(frontier[i].data)
                        exr+=1
        print(res)
        return res
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    
    
    s=input()
    root=buildTree(s)
    ob= Solution()
        
    res = ob.topView(root)
    for i in res:
        print(i,end=" ")
    print()
# } Driver Code Ends