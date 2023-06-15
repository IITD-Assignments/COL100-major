def max_value(V, S):
    l = []
    for i in range(len(V)):
        # V[i] += V[i+S[i]]  # fix C to S
        res = 0  # I added this
        for j in range(len(S)):
            res += V[i] + V[i+S[i]]
        
        l.append(res)

    return max(l)

def max_value_indices(V, S):
    pass
