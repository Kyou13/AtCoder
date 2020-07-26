A, B, C = list(map(int, input().split()))
K = int(input())

# 貪欲法
for _ in range(K):
    if B <= A:
        B = B * 2
    elif C <= B:
        C = C * 2

if A < B and B < C:
    print('Yes')
else:
    print('No')

# 別解：全探索
# flag = False
# for i in range(K):
#     for j in range(K):
#         for k in range(K):
#             x = A * (1 << i)
#             y = B * (1 << j)
#             z = C * (1 << k)
#             if (i + j + k <= K) and x < y and y < z:
#                 flag = True
# if flag:
#     print("Yes")
# else:
#     print("No")
