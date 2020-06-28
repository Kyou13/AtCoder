import math
N, A, B = list(map(int, input().split()))


def sum_of_digits(n):
    res = 0
    while n > 0:
        res += n % 10
        n = math.floor(n / 10)
    return res


total = 0
for i in range(1, N+1):
    s = sum_of_digits(i)
    if s >= A and s <= B:
        total += i
print(total)
