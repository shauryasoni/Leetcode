class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = {}
        for i in range(len(s)) :
            d[i] = False
            
        d[len(s)] =True
        for i in range(len(s)-1,-1,-1) :
            for j in wordDict :
                if len(j) <= len(s[i:]) :
                    if j == s[i:i+len(j)] :
                        d[i] = d[i+len(j)] 
                if d[i] :
                    break
        print(d)
        return d[0]

#This is the dynamic programming approach