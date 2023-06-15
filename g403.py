def max_value(V, S):
    n = len(V)
    dp = [0] * (n + 1)  # I added the brackets

    for i in range(n, -1, -1):
        if n+1-i >= S[i]:
            dp[n+1-i] = max(V[i]+dp[n+1-i-S[i]], dp[n+1-i-1])
        else:
            dp[n+1-i] = dp[n+1-i-1]
    
    return dp[n]

def max_value_indices(V, S):
    pass
