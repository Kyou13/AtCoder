import math
N = int(input())
W = list(map(int, input().split()))
left = [W[0]]
for i in range(1,len(W)-1):
  left.append(W[i]+left[i-1])
right = [W[-1]]
for i in range(len(W)-2,0,-1):
  right.append(W[i]+right[len(right)-1])
res = []
for i in range(len(W)-1):
  res.append(abs(left[i] - right[len(right)-i-1]))
print(min(res))
