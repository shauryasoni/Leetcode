from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        if len(heights) == 1 : 
            return heights[0]
        
        l = len(heights)
        minl  = [-1 for i in range(len(heights))]
        minr = [-1  for i in range(len(heights)) ]
        st = [0]
        index = 0
        for i in range(1,l) :
            while st and heights[i]<heights[st[-1]]:
                minr[st[-1]] = i
                st.pop()
            st.append(i)
            
        st = [l-1]
        for i in range(l-2,-1,-1) :
            while st and heights[i]<heights[st[-1]]:
                minl[st[-1]] = i
                st.pop()
            st.append(i)
        print(minr)
        print(minl)
        mx = 0
        for i in range(l) :
            a = 0
            if minr[i] == -1 and minl[i] == -1 :
                a = heights[i] * (l)
                
            elif minr[i] == -1 :
                a = heights[i] * (l - minl[i] - 1)
                
            elif minl[i] == -1 :
                a = heights[i] * (minr[i])
            else :
                a = heights[i] * (minr[i] - minl[i] - 1)
                
            if a > mx :
                mx = a
        return mx
        
print(Solution().largestRectangleArea([9,0]))      
            
                
                