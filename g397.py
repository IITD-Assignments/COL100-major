def max_value(V, S):
    n = len(V)  # I added this line
    dp = [0] * n
    dp[0] = V[0]
    for i in range(n):
        dp[i] = dp[i-1]
        for j in range(i):
            if i > S[j]:
                dp[i] = max(dp[i], dp[i-j] + V[j])
            else:
                pass
        
    return dp[n-1]

def max_value_indices(V, S):
    # /** I added these lines
    n = len(V)  # I added this line
    dp = [0] * n
    dp[0] = V[0]
    for i in range(n):
        dp[i] = dp[i-1]
        for j in range(i):
            if i > S[j]:
                dp[i] = max(dp[i], dp[i-j] + V[j])
            else:
                pass
    # **/

    g, l = [], []
    for i in range(n-1):
        if dp[i] == dp[i+1]:
            pass
        elif dp[i] != dp[i+1]:
            l.append(V[i])
            g.append(S[i])
    
    for j in range(len(l)):
        t = (l[j], g[j])
        print(t)
