s = input()

def ACGT(s):
  if s in ['A','C','G','T']:
    return True
  else:
    return False

count = 0
result = 0
for c in s:
  if ACGT(c):
    count += 1
    if count > result:
      result = count
  else:
    count = 0

print(result)
