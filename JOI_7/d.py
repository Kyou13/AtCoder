M = int(input())
m = list([tuple(map(int, input().split())) for _ in range(M)])
N = int(input())
n = set([tuple(map(int, input().split())) for _ in range(N)])

for (xn, yn) in n:  # O(n)
    dx = xn - m[0][0]
    dy = yn - m[0][1]
    count = 0
    for (xm, ym) in m:  # O(m)
        if tuple([xm + dx, ym + dy]) in n:  # O(n)
            count += 1
        else:
            break
    if count == M:
        print(dx, dy)
        break
