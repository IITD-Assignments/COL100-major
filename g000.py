def max_value(V, S):
    n = len(V)
    dp = [0] * n
    for i in range(n-1, -1, -1):
        if (i + S[i] + 1) < n:
            dp[i] = max(dp[i+1], V[i] + dp[i+S[i]+1])
        elif (i + 1 < n):
            dp[i] = max(dp[i+1], V[i])
        else:
            dp[i] = V[i]
    
    print(f"DP array: {dp}")

    return dp[0]

def max_value_indices(V, S):
    pass
