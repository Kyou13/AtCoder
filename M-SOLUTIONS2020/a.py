N = int(input())

if N >= 400 and N <= 599:
    print(8)
elif N >= 600 and N <= 799:
    print(7)
elif N >= 800 and N <= 999:
    print(6)
elif N >= 1000 and N <= 1199:
    print(5)
elif N >= 1200 and N <= 1399:
    print(4)
elif N >= 1400 and N <= 1599:
    print(3)
elif N >= 1600 and N <= 1799:
    print(2)
elif N >= 1800 and N <= 1999:
    print(1)

# 別解
# print(10 - int(input()) // 200)
