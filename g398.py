def max_value(V, S):
    l = len(V)
    L = [0 for _ in range(l)]
    L[-1] = V[-1]
    for i in range(l-1, -1, -1):
        S_i = S[i]
        V_i = V[i]
        if i + S_i > l - 1:
            print(i)
            L[i] = max(V_i, L[i+1])
        else:
            L[i] = max(L[i+1], V_i + L[i+S_i+1])
    
    return L[0]

def max_value_indices(V, S):
    l = len(V)
    L = [0 for _ in range(l)]
    L[-1] = (V[-1], 1)
    for i in range(l-1, -1, -1):
        S_i = S[i]
        V_i = V[i]
        if i + S_i > l -1:
            if V_i > L[i+1]:
                L[i] = (V_i, 2)
            else:
                L[i] = (L[i+1], 0)
        else:
            if V_i + L[i + S_i + 1] > L[i + 1]:
                L[i] = (V_i + L[i+S_i+1], 1)
            else:
                L[i] = (L[i+1],0)
        index_list = []
        i = 0
        while i < 1:
            if L[i][1] == 2:
                index_list.append(i)
            elif L[i][1] == 1:
                index_list.append(i)
            else:
                ## scan error, need to refer to the answer script
                pass
