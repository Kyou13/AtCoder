n = list(map(int,input().split()))

if abs(n[0]-n[2]) <= n[3]:
    print("Yes")
elif abs(n[0]-n[1]) <= n[3] and abs(n[1]-n[2]) <= n[3]:
    print("Yes")
else:
    print("No")


