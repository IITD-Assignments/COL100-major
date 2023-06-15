import sys
import importlib


if __name__ == "__main__":
    file_n = f"{sys.argv[1]}"
    mod = importlib.import_module(f"f{file_n}")

    n = int(sys.argv[2])
    print(f"Running {file_n} < {n} ... \n")

    ret = mod.print_pattern(n)
    if ret is not None:
        print(ret)
    