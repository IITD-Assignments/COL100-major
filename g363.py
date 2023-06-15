def max_value(V, S):
    n = len(V) + 1  # I added this
    M = [[None] * n for i in range(n)]  # I added this
    for i in range(n):
        for j in range(n):
            if i == 0 or j == 0:
                M[i][j] = 0
    print(M)

    for i in range(0, n):
        for j in range(i, n):
            if S[i] - n < 0:
                M[i][j] = max(M[i-1][j], M[i][j-1])
                j = j + S[j]
            else:
                M[i][j] = 0
    return M[n][n]

def max_value_indices(V, S):
    pass
