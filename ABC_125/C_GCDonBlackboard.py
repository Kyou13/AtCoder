import math
from functools import reduce as red

def gcd(numbers):
  return red(math.gcd, numbers)

N = int(input())
A = list(map(int, input().split()))

M = []
for i in range(len(A)-1):
  if i != 0:
    L = gcd(A[:i])
  R = gcd(A[i+1:])
  try:
    L
    M.append(math.gcd(L,R))
    del(L)
  except:
    M.append(R)
  del(R)
print(max(M))
