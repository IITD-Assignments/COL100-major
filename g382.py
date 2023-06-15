dp = dict()  # I added this line


def max_value(V, S):
    # dp = {}  ## I commented this line
    if len(V) == 1:
        return V[0]
    elif (V, S) in dp:
        return dp[(V,S)]
    else:
        c_1 = V[0] + max_value(V[S[0] + 1:], S[S[0] + 1:])
        c_2 = max_value(V[1:], S[1:])
        c = max(c_1, c_2)

        dp[(V,S)] = c

        return c


def max_value_indices(V, S):
    pass
