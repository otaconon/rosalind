import sys

def solve(n: int, m: int):
    B = [0] * (n + 1)
    B[0] = 1
    for i in range(1, n):
        B[i+1] = B[i] + B[i-1] - (B[i-m] if i >= m else 0)
    return B[n] + B[n-1]


print(solve(int(sys.argv[1]), int(sys.argv[2])))