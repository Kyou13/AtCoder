from itertools import combinations
N = int(input())
xy = set([tuple(map(int, input().split())) for _ in range(N)])

ans = 0
for (x1, y1), (x2, y2) in combinations(xy, 2):
    dx = x1 - x2
    dy = y2 - y1

    if (x1 + dy, y1 + dx) in xy and (x2 + dy, y2 + dx) in xy:
        ans = max(ans, (dx ** 2) + (dy ** 2))
print(ans)
