N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = []
for _ in range(N):
  A.append(list(map(int, input().split())))
res = 0
for i in range(N):
  tmp = 0
  for j in range(M):
    tmp += A[i][j]*B[j]
  tmp += C
  if tmp > 0:
    res += 1
print(res)
