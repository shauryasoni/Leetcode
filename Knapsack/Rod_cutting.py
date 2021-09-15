class Solution:
    
    #Function to find the maximum number of cuts.
    def maximizeTheCuts(self,n,x,y,z):
        #code here
        dp= [-1 for i in range(n+1)]
        l = [x,y,z]
        dp[0] = 0
        for i in range(1,len(dp)) :
            for j in l :
                if j<=i :
                    if dp[i-j]!=-1 :
                        dp[i] = max(dp[i],dp[i-j] + 1)
        return 0 if dp[n] == -1 else dp[n] 
        