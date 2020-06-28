N, Y = list(map(int, input().split()))


resultA = -1
resultB = -1
resultC = -1
for a in range(N+1):
    for b in range(N+1-a):
        c = N - a - b
        if ((10000 * a + 5000 * b + 1000 * c) == Y):
            resultA = a
            resultB = b
            resultC = c

print("{} {} {}".format(resultA, resultB, resultC))
