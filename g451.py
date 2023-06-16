def max_value(V, S):
    n = len(V)  # I added this line
    lookup = [V[-1]]
    for i in range(len(V)-1,-1,-1):
        S_i = S[i]
        if (i + S_i < len(V)):
            lookup.append(V[i] + lookup[n-1-i-S_i])
        else:
            lookup.append(V[i])

    return lookup[-1]

def max_value_indices(V, S):
    pass
