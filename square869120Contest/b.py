import copy
import math
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

# 部分点
# res = float('inf')
# for i in range(1, 101):
#     for o in range(1, 101):
#         tmp = 0
#         for ab in AB:
#             tmp += abs(i - ab[0]) + abs(ab[0] - ab[1]) + abs(o - ab[1])
#         if tmp < res:
#             res = tmp

# 満点回答
# TODO
# AB.sort(key=lambda x: x[0])
# a_sorted = copy.deepcopy(AB)
# AB.sort(key=lambda x: x[1])
# b_sorted = copy.deepcopy(AB)
# if N % 2 == 0:
#     i = a_sorted[N/2][0]
#     o = b_sorted[N/2][1]
# else:
#     i = a_sorted[math.floor(N/2)][0]
#     o = b_sorted[math.floor(N/2)][1]
# res = 0
# for ab in AB:
#     res += abs(i - ab[0]) + abs(ab[0] - ab[1]) + abs(o - ab[1])

res = float('inf')
for i in AB:
    for o in AB:
        tmp = 0
        for ab in AB:
            tmp += abs(i[0] - ab[0]) + abs(ab[0] - ab[1]) + abs(o[1] - ab[1])
        if tmp < res:
            res = tmp
print(res)
