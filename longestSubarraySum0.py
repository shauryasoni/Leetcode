class Solution:
    def maxLen(self, n, arr):
        #Code here
        prefix = {}
        s = 0
        m = 0
        for i in range(len(arr)) :
            s = s+arr[i]
            if s == 0 :
                l = i + 1
                if l > m:
                    m = l
            else :
                if s in prefix :
                    l = i - prefix[s] 
                    if l > m :
                        m = l
                else :
                    prefix[s] = i
        return m