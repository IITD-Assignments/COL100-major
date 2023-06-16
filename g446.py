def max_value(V, S):
    n = len(V)
    dp = [0] * n
    dp[0] = V[0]
    for i in range(1,n):
        for j in range(i):
            if (j+S[j] < i):
                dp[i] = max(dp[i], V[i] + dp[j])
            else:
                dp[i] = max(dp[i], dp[j])
    
    return dp[n-1]

def max_value_indices(V, S):
    n = len(V)
    dp = [0] * n
    dp[0] = V[0]
    indices = []
    for i in range(1,n):
        max_i = dp[i]
        flag = 0
        for j in range(i):
            if (j + S[j] < i):
                if (V[i] + dp[j] > max_i):
                    max_i = V[i] + dp[j]  # I changed 'max' to 'max_i'
                    dp[i] = max_i
                    flag = 1
                else:
                    if dp[j] > max_i:
                        max_i = dp[j]
                        flag = 0
        
        if flag:
            indices.append(i)

    return dp[n-1], indices