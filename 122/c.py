n, q = map(int, input().split())
s = input()

lr = list()
for _ in range(q):
  lr.append(list(map(int, input().split())))

tmp = [0]
count = 0
for i in range(n-1):
  if s[i:i+2] == 'AC':
    count += 1
    tmp.append(count)
  else:
    tmp.append(tmp[i])

for l,r in lr:
  print(tmp[r-1]-tmp[l-1])
