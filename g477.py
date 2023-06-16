def max_value(V, S):
    M = [-1 for i in range(len(V))]
    for i in range(len(M)):
        if S[i] >= len(M)-i-1:
            M[i] = V[i]
    
    for i in range(-1, -len(M), -1):  # I split '-len(M)-1' into '-len(M)' and '-1'
        if M[i] == -1:
            M[i] = V[i] + max(M[i+S[i]+1])
    
    return max(M)

def max_value_indices(V, S):
    pass
