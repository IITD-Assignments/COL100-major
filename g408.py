def max_value(V, S):
    if len(V) == 1:
        return V[0]
    else:
        if V[0] + max_value(V[S[0]+1:], S[S[0]+1:]) > max_value(V[1:], S[1:]):
            return V[0] + max_value(V[S[0]+1:], S[S[0]+1:])
        else:
            return max_value(V[1:], S[1:])

def max_value_indices(V, S):
    if len(V) == 1:
        return V, V[0]
    else:
        if V[0] + max_value(V[S[0]+1:], S[S[0]+1:]) > max_value(V[1:], S[1:]):
            return [V[0]], V[0] + max_value(V[S[0]+1:], S[S[0]+1:])
        else:
            return max_value(V[1:], S[1:])
