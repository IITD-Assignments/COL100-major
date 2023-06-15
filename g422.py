def max_value(V, S):
    if len(V) == 0:
        return 0
    elif len(V) == 1:
        return V[0]
    else:
        k = []
        for i in range(0, len(V)):
            k.append(V[i] + max_value(V[i+S[i]+1:], S[i+S[i]+1:]))
    
    max_index = 0
    for j in range(len(k)):
        if k[j] > k[max_index]:
            max_index = j
    
    return k[max_index]

def max_value_indices(V, S):
    pass
