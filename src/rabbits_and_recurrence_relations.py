import sys

def solve(new_born, reproduction, n, k) -> int:
    if n == 1:
        return new_born + reproduction
    return solve(reproduction*k, reproduction+new_born, n-1, k)

print(solve(1, 0, int(sys.argv[1]), int(sys.argv[2])))