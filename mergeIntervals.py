from typing import List
#create an array for all times. Mark as 1 if it is an interval. In the end, count groups of 1's and return interval
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sl = sorted(intervals,key=lambda x : x[0])
        mn = intervals[0][0]
        mx = intervals[0][1]
        for i in intervals :
            if i[0] < mn :
                mn = i[0]
            if i[1] > mx :
                mx = i[1]
        #print(mn,mx)
        n = mx-mn + 1
        result = []
        l = [0 for i in range(mx+1)]
        for i in intervals :
            start = i[0]
            end = i[1]
            if start == end :
                if l[start] == 1 :
                    continue
                else :
                    l[start] = 0.5
           # print(start,end)
            for j in range(start,end) :
                l[j]=1
        index = 0
        s = -1
        print (l)
        for i in range(len(l)) :
            if l[i] == 1 and s==-1 :
                s = i
            if l[i] == 0 and s!=-1 :
                result.append([s,i])
                s = -1
            if i == len(l)-1 :
                if l[i] == 1 and s!=-1 :
                    result.append([s,i])
                if l[i] == 1 and s == -1 :
                    result.append([i,i])
                
            if l[i] == 0.5 and s==-1:
                result.append([i,i])
            if l[i] ==0.5 and s!=-1 :
                result.append([s,i])
                s = -1

        return result    
            
"""
this solution involves sorting the input array :

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result=[]
        for interval in intervals:
            first =interval[0]
            second=interval[1]
            if len(result)== 0 :
                result.append(interval)
            elif result[-1][0] == first:
                result.pop(-1)
                result.append(interval)
            elif first <= result[-1][1]:
                first  = result[-1][0]
                second= max(second,result[-1][1])
                result.pop(-1)
                result.append([first,second])
            else:
                result.append(interval)
        return result
"""          
            