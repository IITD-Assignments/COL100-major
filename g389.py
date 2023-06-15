def max_value(V, S):
    n = len(V)  # I added this line
    L = [None] * n
    S_0 = max(S)
    for i in range(S_0 + 2):
        L.append(0)
    j = n-1
    while j >= 0:
        L[j] = max(L[j+1], j+S[j]+1)
        L[j] = max(L[j], V[j] + L[j + S[j] + 1])

    return L[0]

def max_value_indices(V, S):
    n = len(V)  # I added this line
    L = [None] * n
    S_0 = max(S)
    for i in range(S_0 + 2):
        L.append(0)
    j = n-1
    while j >= 0:
        L[j] = max(L[j+1], j+S[j]+1)
        L[j] = max(L[j], V[j] + L[j + S[j] + 1])

    return L[0]
