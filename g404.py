def max_value(V, S):
    n = len(V)  # I added this line
    dp = [-1] * n
    dp[n-1] = V[n-1]
    i = n-1
    while (i >= 0):
        if dp[i] != -1:
            return dp[i]
        else:
            m = -1
            for j in range(S[i]):
                if i - j >= 0:
                    m = max(m, dp[i-j] + V[i-j])
            
            dp[i] = m
    
    return dp[0]

def max_value_indices(V, S):
    pass
