def max_value(V, S):
    max_list = [0 for i in range(len(V))]
    max_list[len(V)-1] = max(V[len(V)-1], 0)
    for i in range(len(V)-2, -1, -1):
        if S[i] + i + 1 >= len(V):
            max_list[i] = max_list[i+1]
        else:
            max_list[i] = max(max_list[i+1], max_list[i+S[i]]+V[i])
    
    return max_list[0]

def max_value_indices(V, S):
    pass
