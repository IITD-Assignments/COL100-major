def max_value(V, S):
    dp = [0 for i in range(len(V) + 1)]
    dp[-1] = V[-1]
    for i in range(len(V), 0, -1):  # I added the -1 step-size, and removed -1 from len(V)
        if i + S[i-1] < len(dp):
            max_x = max(V[i-1]+dp[i+S[i-1]], dp[i+1])
            dp[i] = max_x
        else:
            dp[0] = V[i-1]
    
    return dp[1]


def max_value_indices(V, S):
    pass
