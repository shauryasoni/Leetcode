from typing import List
class Solution:
    
    #res = []

    def __init__(self):
        self.res = []
    
    def tree(self,s,n,x,y) : 
        if (x<n and x>=y) :
            
            self.tree(s+"(",n,x+1,y)
        if(y<n and x>=y) : 
            
            self.tree(s+")",n,x,y+1)
            
            
        else :
            if(len(s)==2*n): 
                self.res.append(s)
                #print(s)
            return
    
    
    def generateParenthesis(self, n: int) -> List[str]:
        
        if n == 1 :
            return ["()"]
        
        else : 
            
            
            self.tree("(",n,1,0)
            return self.res
        
        
print(Solution().generateParenthesis(3))