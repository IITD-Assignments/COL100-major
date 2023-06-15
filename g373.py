def max_value(V, S):
    if len(V) == 0 or len(S) == 0:
        return 0
    elif len(V) == 1 or len(S) == 0:
        return V[0]
    else:
        a1 = V[0] + max_value(V[S[0] + 1:], S[S[0] + 1:])
        a2 = max_value(V[1:], S[1:])
    
        return max(a1, a2)

def max_value_indices(V, S):
    if len(V) == 0 or len(S) == 0:
        return 0
    elif len(V) == 1 or len(S) == 1:
        return V[0]
    else:
        t = []
        a1 = V[0] + max_value(V[S[0] + 1:], S[S[0]+1:])
        a2 = max_value(V[1:], S[1:])

        if a1 - V[0] > a2:
            t.append(1 + S[0])
        
        return max(a1, a2), t
