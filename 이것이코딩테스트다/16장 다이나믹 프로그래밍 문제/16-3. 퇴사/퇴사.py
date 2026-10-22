def solution(n, consultations):
    dp = [0] * (n + 1)

    for i in range(n - 1, -1, -1):
        t, p = consultations[i]

        if i + t <= n:
            dp[i] = max(dp[i + 1], p + dp[i + t])
        else:
            dp[i] = dp[i + 1]

    return dp[0]
