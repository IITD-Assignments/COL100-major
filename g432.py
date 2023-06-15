def max_value(V, S):
    dp = [0 for i in range(len(V) + 1)]
    n = len(V)
    dp[1] = V[0]
    for i in range(2, n+1):
        if i - 1 - S[i-1] >= 0 and dp[i-1-S[i-1]] != 0:
            if V[i-1] + dp[i-1-S[i-1]] > dp[i-1]:
                dp[i] = V[i-1] + dp[i-1-S[i-1]]
            else:
                dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1]
    
    return dp[n]

def max_value_indices(V, S):
    def summ(V):
        if len(V) == 0:
            return 0
        else:
            tot = 0
            for i in V:
                tot += V[i]
            
            return tot

    n = len(V)
    dp = [[] for i in range(len(V) + 1)]
    dp[1] = [V[0]]

    for i in range(1, n+1):
        if i - 1 - S[i-1] >= 0:
            if dp[i-1-S[i-1]] != []:
                if V[i] + summ(dp[i-1-S[i-1]]) > summ(dp[i-1]):
                    dp[i] = [V[i]] + dp[i-1-S[i-1]]
                else:
                    dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1]

    idx = []
    for i in dp[n]:
        idx.append(V.under(i))
    
    return (summ(dp[n]), idx)
