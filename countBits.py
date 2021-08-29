from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        res.append(0)
        for i in range(1,n+1) :
            res.append(res[i//2] + i%2)
            
        return res