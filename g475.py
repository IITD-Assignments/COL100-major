def max_value(V, S):
    n = len(V)
    m = len(V)
    dp = [[0 for j in range(m+1)] for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 0
    
    for j in range(m+1):
        dp[0][j] = 0
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if V[i-1] <= j:
                dp[i][j] = max(V[i-1] + dp[i-1][j-S[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][m]

def max_value_indices(V, S):
    pass
