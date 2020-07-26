import math
n = int(input())
A = list(map(int, input().split()))
q = int(input())
m = list(map(int, input().split()))

sub_set = set()
for i in range(int(math.pow(2, n))):
    tmp_sum = 0
    for j in range(n):
        if((i >> j & 1) == 1):
            print(i, j)
            tmp_sum += A[j]
    sub_set.add(tmp_sum)

for i in m:
    print("yes" if i in sub_set else "no")
