N, M = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(0, M-1):
    for j in range(i+1, M):
        tmp = 0
        for a in A:
            tmp += max(a[i], a[j])
        if tmp > result:
            result = tmp

print(result)
