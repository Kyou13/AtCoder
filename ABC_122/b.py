S = input()

ACGT = 'A C G T'.split()
result = 0
tmp = 0
for i in S:
    if i in ACGT:
        tmp += 1
    else:
        tmp = 0
    if tmp > result:
        result = tmp

print(result)
