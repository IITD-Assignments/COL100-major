def max_value(V, S):
    n = len(V)
    d = {}
    def dp(i, n):
        if i >= n:
            return 0
        if i in d:
            return d[i]
        
        a = max(V[i] + dp(i+S[i], n), dp(i+1, n))
        d[i] = a

        return a

    return dp(0, n)

def max_value_indices(V, S):
    pass
