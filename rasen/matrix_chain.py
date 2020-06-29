N = int(input())
p = [0] * (N+1)
for i in range(1, N+1):
    p[i-1], p[i] = list(map(int, input().split()))

m = [[0] * (N+1) for i in range(N+1)]

for l in range(2, N+1):  # 対象の行列数を2からNまで増やす
    for i in range(1, N - l + 2):
        j = i+l-1
        m[i][j] = float('inf')
        for k in range(i, j):
            m[i][j] = min(m[i][j],
                          m[i][k] + m[k + 1][j] + p[i-1] * p[k] * p[j])

print(m[1][N])
