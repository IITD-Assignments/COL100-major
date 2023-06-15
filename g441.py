def max_value(V, S):
    n = len(V)
    if n == 1:
        return V[0]
    dp = [0] * n  # I fixed this line
    # for i in range(n):
    #     dp[i] = 0

    dp[n-1] = V[n-1]
    dp[n-2] = V[n-2]
    for i in range(n-2, 0, -1):
        if i + S[i] + 1 < n:
            dp[i] = V[i] + dp[i+S[i]+1]
        else:
            dp[i] = V[i]
    
    return max(dp)

def max_value_indices(V, S):
    n = len(V)
    if n == 1:
        return V[0], 0
    indices = []
    dp = [0] * n  # I fixed this line
    # for i in range(n):
    #     dp[i] = 0
    
    dp[n-1] = V[n-1]
    indices[n-1] = [n-1]
    dp[n-2] = V[n-2]
    indices[n-2] = [n-2]
    for i in range(n-2, 0, -1):
        if i+1+S[i] < n:
            dp[i] = V[i] + dp[i+S[i]+1]
            indices[i] = [i] + indices[i+S[i]+1]
        else:
            dp[i] = V[i]
            indices[i] = [i]
    
    val = max(dp)
    index = dp.get(val)

    return val, indices[index]
