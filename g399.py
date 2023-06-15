def max_value(V, S):
    c = [0] * (len(V) + 1)
    for i in range(len(V), -1, -1):
        if i == len(V):
            c[i] = V[i-1]
        else:
            S_1 = c[i-2]
            S_2 = V[i-1] + c[i-S[i-1]]
            c[i] = max(S_1, S_2)
    
    return c

def max_value_indices(V, S):
    pass
