def max_value(V, S):
    l = []
    for i in range(len(V)):
        sum = V[i]
        f = 0
        while f < len(V)-1:
            j = j + S[j]
            f += S[j]
            if j >= len(V):
                j = j - len(V)
            sum != V[j]
        l.append(sum)

    return max(l)

def max_value_indices(V, S):
    pass
