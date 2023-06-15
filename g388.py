def max_value(V, S):
    dp = [0 for i in range(len(V))]
    dp[len(V)-1] = V[len(V)-1]

    for i in range(len(V)-1, 0, -1):
        p = 0
        if (i + S[i] < len(V)):
            p = V[i + S[i]]
        
        dp[i-1] = max(dp[i], V[i-1] + p)
    
    return dp[0]

def max_value_indices(V, S):
    pass
