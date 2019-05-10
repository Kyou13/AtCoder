S = list(map(int, list(input())))

N = len(S)
black_start = [0 if i%2 else 1 for i in range(N)]
white_start = [1 if i%2 else 0 for i in range(N)]

res_0 = 0
res_1 = 0
for i, j in zip(S, black_start):
  if i != j:
    res_0 += 1
for i, j in zip(S, white_start):
  if i != j:
    res_1 += 1
print(min(res_0, res_1))
