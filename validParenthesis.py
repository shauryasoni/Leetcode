class Solution:
    def __init__(self) :
        self.ans = set()
    def rec(self,l,r,s,d) :
       
        if (s,l,r) in d :
            return d[(s,l,r)]
        if s=="" and l==r :
            return True
        if s=="" and l!=r :
            return False
        if r > l :
            return False
       
        if s[0] == "(" :
            if len(s)!=1 :
                d[(s,l,r)] = self.rec(l+1,r,s[1:],d)
                return d[(s,l,r)]
            else :
                d[(s,l,r)] = self.rec(l+1,r,"",d)
                return d[(s,l,r)]
        elif s[0] == ")" :
            if len(s)!=1 :
                d[(s,l,r)] = self.rec(l,r+1,s[1:],d)
                return d[(s,l,r)]
            else :
                d[(s,l,r)] = self.rec(l,r+1,"",d)
                return d[(s,l,r)]
        else :
            if len(s)!=1 :
                d[(s,l,r)] =  self.rec(l+1,r,s[1:],d) or self.rec(l,r+1,s[1:],d) or self.rec(l,r,s[1:],d)
                return d[(s,l,r)]
            else :
                d[(s,l,r)] = self.rec(l+1,r,"",d) or self.rec(l,r+1,"",d) or self.rec(l,r,"",d)        
                return d[(s,l,r)]
   
    def checkValidString(self, s: str) -> bool:
        if s == "*" :
            return True
        if len(s)==0 :
            return False
        elif len(s) == 1 :
            return False
        elif s[0]==")" :
            return False
        else :
            d = {}
            return self.rec(0,0,s,d)
print(Solution().checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"))