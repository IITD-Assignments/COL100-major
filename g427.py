def max_value(V, S):
    sum = 0
    dp = []
    if len(V) == 0:
        return sum
    # for i in range(len(V)):
    #     dp.append()
    else:
        S_1 = V[0]
        a_1 = S[0] + 1
        max_value(V[a_1:], S[a_1:])

        S_2 += V[1]
        a_2 = S[1] + 1
        max_value(V[a_2:], S[a_2:])
        sum = max(S_1, S_2)
    
    return sum

def max_value_indices(V, S):
    pass
