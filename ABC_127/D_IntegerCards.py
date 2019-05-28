N, M = map(int, input().split())
A = list(map(int, input().split()))
X = []
for _ in range(M):
  B, C = map(int, input().split())
  X.append([B,C])
X = sorted(X, key=lambda x: x[1], reverse=True)
A = sorted(A)

flag = 0
for _ in range(N):
  if A[flag] < X[0][1]:
    A[flag] = X[0][1]
    X[0][1] = X[0][1]-1
    flag += 1
    if X[0][1] == 0:
      del(X[0])

print(sum(A))
