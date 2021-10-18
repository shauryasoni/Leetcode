def climb(n,s) :
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(len(dp)) :
        for j in range(1,s+1) :
            if i-j < 0 :
                break
            else :
                dp[i] = dp[i-j] + dp[i]
    return dp[n]
print(climb(6,2))