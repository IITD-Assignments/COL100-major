def max_value(V, S):
    def recursive_max_value(V,S):
        if len(V) == 0:
            return 0
        elif len(V) == 1:
            return V[0]
        else:
            return max(
                V[len(V)-1] + recursive_max_value(V[:len(V)-S[len(V)-1]], S), 
                recursive_max_value(V[:len(V)-1], S))
    
    def max_val(V, S):
        n = len(V)
        i = 0
        dp = []
        while i < n+1:
            if (i==0):
                dp.append(0)
            elif i == 1:
                dp.append(V[0])
            else:
                dp.append(-1)
            
            i += 1  # I added this line
            
        i = 2
        while i < n + 1:
            dp[i] = max(V[n-1] + dp[i - S[n-1]], dp[i-1])
        
        return dp[n]
    
    # return recursive_max_value(V, S)  # I added this line
    return max_val(V, S)  # I added this line

def max_value_indices(V, S):
    pass
