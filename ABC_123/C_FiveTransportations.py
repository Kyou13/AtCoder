import math
N = int(input())
A,B,C,D,E = [int(input()) for _ in range(5)]
min_road = min(A,B,C,D,E)
if min_road >= N:
  res = 5
else:
  res = math.floor((N-1)/min_road)+5
  import pdb;pdb.set_trace()
print(res)
