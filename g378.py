def max_value(V, S):
    L = [[0 for i in range(len(V) + 1)] for j in range(len(S) + 1)]
    for i in range(len(S) + 1):
        for j in range(len(V) + 1):
            t = 0
            if S[i] >= t:
                L[i][j] = L[i-1][j-1]
                t = t+1
            else:
                L[i][j] += L[i-t][j-t]

    return

def max_value_indices(V, S):
    pass
