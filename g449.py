def max_value(V, S):
    if len(V) == 0:
        return 0
    elif len(V) == 1:
        return V[0]
    else:
        for i in range(len(V)):
            k = V[0]
            for j in range(S[i]):
                V.pop(i+1)
        
        return max(k+max_value(V[1:], S[1:]))

def max_value_indices(V, S):
    pass
