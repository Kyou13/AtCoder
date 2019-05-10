N = int(input())
H = list(map(int, input().split()))

res = 1
for i in range(1,N):
  tmp = 0
  for j in range(i):
    if H[i] >= H[j]:
      tmp += 1
  if tmp == i:
    res += 1
print(res)
