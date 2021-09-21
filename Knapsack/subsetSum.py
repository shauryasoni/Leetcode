class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here 
        dp =[ [False for i in range(sum+1)] for i in range(len(arr) + 1)  ]
        r = len(dp)
        c = len(dp[0])
        for i in range(r) :
            dp[i][0] = True
        
        for i in range(1,r) :
            for j in range(1,c) :
                if arr[i-1] > j :
                    dp[i][j] = dp[i-1][j]
                
                else :
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
        return dp[r-1][c-1]