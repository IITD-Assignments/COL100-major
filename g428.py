def max_value(V, S):
    dp = {}
    def max_val(V, S):
        max_v = 0  # I put this line here
        if len(V) == 0:
            return 0
            # max_v = 0
        elif max_v in dp:
            return max_v
        else:
            for i in V:
                for j in S:
                    max_v = max(V[j])
                    dp = max_v

def max_value_indices(V, S):
    pass
