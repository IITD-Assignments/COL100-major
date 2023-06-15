import sys
import importlib


if __name__ == "__main__":
    file_n = f"{sys.argv[1]}"
    mod = importlib.import_module(f"g{file_n}")

    print(f"Running {file_n} ... \n")

    V = [4, 3, 1, 2, 1]
    S = [2, 1, 1, 1, 1]

    ret_1 = mod.max_value(V, S)
    if ret_1 is not None:
        print(ret_1)

    ret_2 = mod.max_value_indices(V, S)
    if ret_2 is not None:
        print(ret_2)
