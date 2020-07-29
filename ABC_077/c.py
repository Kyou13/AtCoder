import bisect
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))


a.sort()
c.sort()
sum_count = 0
for i in b:
    sum_count += bisect.bisect_left(a, i) * (N - bisect.bisect_right(c, i))
print(sum_count)
