N, M = list(map(int, input().split()))
xy = set([tuple(map(int, input().split())) for _ in range(M)])

res = 0
for i in range(2 ** N):
    faction = []
    for j in range(N):
        if(i & (1 << j)):
            faction.append(j)

    flag = True
    for j in range(len(faction)-1):
        for k in range(j+1, len(faction)):
            relation = faction[j], faction[k]

            if(relation not in xy):
                flag = False
                break
        if(not flag):
            break

    if(flag):
        res = max(res, len(faction))

print(res)
