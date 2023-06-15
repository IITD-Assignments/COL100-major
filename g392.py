def max_value(V, S):
    def sum(V, S, i=0, memo={}):
        if i == len(V):
            return 0
        elif i in memo:
            return memo[i]
        else:
            memo[i] = max(sum(V,S,i+1, memo), 
                          V[i] + sum(V, S, i+1+S[i], memo))
            return memo[i]

    return sum(V, S, 0, {})

def max_value_indices(V, S):
    def sum(V, S, i=0, memo={}):
        if i == len(V):
            return 0, memo
        elif i in memo:
            return memo[i], memo
        else:
            memo[i] = max(sum(V,S,i+1, memo), 
                          V[i] + sum(V, S, i+1+S[i], memo))
            return memo[i], memo

    m = sum(V, S)[0]
    d = sum(V, S)[1]
    indices = []
    for x in range(len(V)-1, 0, -1):
        if d[x] != d[x-1]:
            pass
