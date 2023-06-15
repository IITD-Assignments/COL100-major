def max_value(V, S):
    def foo(V, S, i=0, memo={}):
        if i in memo:
            return memo[i]
        if i >= len(V):
            return 0
        else:
            memo[i] = max(V[i]+foo(V, S, i+S[i]+1, memo), foo(V, S, i+1, memo))
            return memo[i]
    
    return foo(V, S)

def max_value_indices(V, S):
    def foo(V, S, i=0, memo={}):
        if i in memo:
            return memo[i]
        if i >= len(V):
            return 0
        else:
            memo[i] = max(V[i] + foo(V, S, i+S[i]+1, memo), foo(V, S, i+1, memo))
            return memo
    
    dict = foo(V,S)
    max_value = max(list(dict.values()))
    return max_value, dict[max_value]
