def solution(n, k):
    dp = [0] * n
    dp[0] = k[0]
    dp[1] = max(k[0],k[1])
    
    for i in range(1, len(k)):
        dp[i] = max(dp[i - 1], dp[i - 2] + k[i])
        
    return dp[n - 1]
