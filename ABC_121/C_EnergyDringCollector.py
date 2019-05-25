N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

AB = sorted(AB, key=lambda x:x[0])

res = 0
for i in range(N):
  if AB[i][1] >= M:
    res += M * AB[i][0]
    break
  else:
    res += AB[i][1] * AB[i][0]
    M -= AB[i][1]
print(res)
