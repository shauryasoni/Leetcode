from typing import List
class Solution:


    def wordBreak(self, s: str, wordDict: List[str], memo = {}) -> bool:
        
        if(s in memo.keys())  :
            return memo[s]

        if(s == " "*len(s)) : 
            return True
        match = False
        for i in wordDict :
            if i in s :
                match  = True
                break
        if match ==False :
            return False  

        ans = []
        for i in wordDict : 
            if i in s : 
                new = s.replace(i," "*len(i),1)
                value =( self.wordBreak(new,wordDict,memo)) 
                memo[new] = value
                ans.append(value)
                if value == True :
                    break
        if True in ans : 
            return True 
        else :
            return False

obj = Solution()
print(obj.wordBreak("cars",["car","ca","rs"]))