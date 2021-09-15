from typing import List
class Solution:

    
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        d = {}
        for i in arr :
            if i not in d :
                d[i] = 1
            else :
                d[i]+=1
        
        l = sorted(d.values())[::-1]
        s = 0
        for i in range(len(l)) :
            s+=l[i]
            if s >=n//2 :
                return (i+1)
        return n
