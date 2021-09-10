from typing import List
from collections import deque

#Solved Using Queues
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        q = deque([])
        s = 0
        count = 0
        mincount = len(nums)+1
        n = len(nums)-1
        for i in range(len(nums)) :
            q.append(nums[i])
            #print(q)
            s = s + nums[i]
            count +=1
            while s>=target :
                if count < mincount :
                    mincount = count
                ele = q.popleft()
                s = s-ele
                count = count - 1
            
        if mincount == n+2 :
            return 0
        else :
            return mincount