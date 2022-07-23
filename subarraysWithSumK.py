class Solution:
    # def rec(self, nums, i,s,k,count) :    
    def subarraySum(self, nums: List[int], k: int) -> int:
        h = {}
        h[0] = 1
        count = 0
        pref = 0
        for i in range(len(nums)) :
            pref += nums[i]
            
            if pref - k in h :
                count += h[pref-k]
                
            if pref in h :
                h[pref] += 1
            else :
                h[pref] = 1
        return count
        
#         h = {}
#         h[-1] = 0
#         h[0] = nums[0]
#         for i in range(1,len(nums)) :
#             h[i] = h[i-1] + nums[i]
        
#         count = 0
#         for i in range(len(nums)) :
#             for j in range(i, len(nums)) :
                
#                 if h[j] - h[i-1] == k :
#                     count +=1
                
#         return count
        
