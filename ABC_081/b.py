N = int(input())
A = list(map(int, input().split()))

result = float('inf')
for a in A:
    count = 0
    tmp = a
    while tmp % 2 == 0:
        tmp /= 2
        count += 1
    if count < result:
        result = count

print(result)
