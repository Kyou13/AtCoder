# 最長共通部分列
def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0] * (n+1)] * (m+1)

    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i+1][j+1] = c[i][j] + 1
            else:
                c[i+1][j+1] = max(c[i][j+1], c[i+1][j])

    return c[-1][-1]


M = input()
N = input()
print(lcs(M, N))
