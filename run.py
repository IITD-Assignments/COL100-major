import sys
import importlib


if __name__ == "__main__":
    file_n = f"{sys.argv[1]}"
    mod = importlib.import_module(f"g{file_n}")

    print(f"Running {file_n} ... \n")

    V = [4, 3, 1, 2, 1]
    S = [2, 1, 1, 1, 1]
    ret = mod.max_value(V, S)
    if ret is not None:
        print(ret)
    