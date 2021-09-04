from typing import List
class Solution:

    def wordBreak(self, s: str, wordDict: List[str],memo={}) -> bool:
        if(s == " "*len(s)) : 
            return True
        match = False
        for i in wordDict :
            if i in s :
                match  = True
                break
        if match ==False :
            return False  

        if(s in memo.keys())  :
            return memo[s]
        
        ans = set()
        for i in wordDict : 
            if i in s :  
                new = s.replace(i," "*len(i),1)
                value =( self.wordBreak(new,wordDict,memo)) 
                if new not in memo.keys():
                    memo[new] = value
                ans.add(value)
                if value == True :
                    break

        if True in ans : 
            return True 
        else :
            return False
print(Solution().wordBreak("catsanddogs",["cats","san","dogs"]))