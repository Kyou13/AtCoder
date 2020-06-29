# フィボナッチ数列
N = int(input())


# ただの再帰ver
def fibonacci(n):
    if n in [0, 1]:
        return 1
    else:
        return fibonacci(n-2) + fibonacci(n-1)


F = [-1] * (N+1)
F[0] = 1
F[1] = 1


# メモ化
def fibonacci_memo(n):
    if F[n] != -1:
        return F[n]
    else:
        F[n] = fibonacci_memo(n-2) + fibonacci_memo(n-1)
        return F[n]


print(fibonacci_memo(4))
