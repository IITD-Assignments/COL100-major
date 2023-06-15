def max_value(V, S):
    p = []
    for j in range(len(V)):
        val = 0
        for i in range(j, len(V)):
            val += V[i]
            i += S[i] + 1
        p.append(val)
    
    return max(p)


def max_value_indices(V, S):
    p = []
    for j in range(len(V)):
        val = 0
        for i in range(j, len(V)):
            val += V[i]
            i += S[i] + 1
        p.append(val)
    
    A = []
    x = max(p)
    y = p.index(x)
    for i in range(y, len(V)):
        A.append(i)
        i += S[i] + 1
    
    return x, A
