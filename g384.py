def max_value(V, S):
    n = len(V)
    dp = [0 for i in range(n)]

    for i in range(n-1, -1, -1):
        if (i + S[i] + 1) < n:
            dp[i] + V[i] + dp[i+S[i]+1]
        else:
            dp[i] = V[i]
        
        for j in range(1, i):
            dp[i] = max(dp[i], dp[i-j])

    return dp[0]

def max_value_indices(V, S):
    pass
