import sys
import math

def solve(k:int, m:int, n:int):
   omega = math.comb(k+m+n, 2)
   p = math.comb(k, 2) + k*m + math.comb(m, 2)*0.75 + k*n + m*n*0.5
   return p/omega

print(solve(*map(int, sys.argv[1:])))