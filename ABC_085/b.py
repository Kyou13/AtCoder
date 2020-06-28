N = int(input())
d = [int(input()) for i in range(N)]

num = [0] * 100

for i in d:
    num[i-1] = 1

print(sum(num))
