def max_value(V, S):
    dp = [[0 for i in range(len(V) + 1)] for j in range(len(S) + 1)]
    for i in range(len(S) + 1):
        for j in range(len(V) + 1):
            if (S[i-1] + j > len(V) + 1):
                if (S[i-1] + j > len(V) + 1):
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-S[i-1]][j-V[j-1]] + V[j-1], dp[i-1][j-1])

    return dp[len(S)][len(V)]

def max_value_indices(V, S):
    pass
