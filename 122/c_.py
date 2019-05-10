n, q = map(int, input().split())
s = input()

lr = list()
for _ in range(q):
  lr.append(list(map(int, input().split())))

def calc(s):
  # count = 0
  s_1 = [s[idx:idx+2]for idx in range(0,n,2)]
  s_1.extend([s[idx:idx+2]for idx in range(1,n,2)])
  count = s_1.count('AC')
  return count
for l,r in lr:
  print(calc(s[l-1:r]))
