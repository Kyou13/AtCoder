import math
N, M = map(int, input().split())
s=[]
for _ in range(M):
  tmp = list(map(int, input().split()))
  s.append(tmp[1:])
p = list(map(int, input().split()))

all_switches = ['0'*(N - len(bin(i)[2:]))+bin(i)[2:] for i in range(pow(2,N))]

res = 0
for i in all_switches:
  p_count = 0
  for j,k in zip(s,p):
    tmp = 0
    for l in j:
      tmp += int(i[N - l])
    if (tmp % 2) == k:
      p_count += 1
  if len(p) == p_count:
    res += 1
print(res)
