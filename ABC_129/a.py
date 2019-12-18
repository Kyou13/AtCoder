P,Q,R = list(map(int, input().split()))
ans = []
ans.append(P+Q)
ans.append(P+R)
ans.append(Q+R)
print(min(ans))
