result = []
while True:
    n, x = list(map(int, input().split()))
    if n == 0 and x == 0:
        break
    count = 0

# 3重ループ
#     for i in range(1, n-1):
#         for j in range(i+1, n):
#             for k in range(j+1, n+1):
#                 print(i, j, k)
#                 if i + j + k == x:
#                     count += 1

# 2重ループ
    for i in range(1, n-1):
        for j in range(i+1, n):
            tmp = x - i - j
            if tmp <= n and tmp > j:
                count += 1

    result.append(count)
print(result)
