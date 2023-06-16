def max_value(_V, _S):
    dp = ["/"] * (len(_V)-1)
    
    def funct(V,S,dp,m):
        if m == (len(V) - 1):
            dp[m] = V[m]
            return dp[m]
        elif S[m] + 1 > len(V[m+1:]):
            dp[m] = V[m]
            return dp[m]
        else:
            if dp[m] != "/":
                return dp[m]
            else:
                dp[m] = V[m] + funct(V, S, dp, m + S[m] + 1)
                return dp[m]
    
    m = []
    for i in range(0, len(_V)):
        c = funct(_V, _S, dp, i)
        m.append(c)

    return max(m)

def max_value_indices(V, S):
    pass
