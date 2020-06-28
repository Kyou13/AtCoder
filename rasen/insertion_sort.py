# 挿入ソート
# 昇順

N = int(input())
A = list(map(int, input().split()))


def trace(A, N):
    for c, i in enumerate(A):
        if c > 0:
            print(" ", end='')
        print(i, end='')
    print("")


def test(A, N):
    tmp = 0
    for i in range(1, N):
        tmp = A[i]
        j = i - 1
        while(j >= 0 and A[j] > tmp):
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = tmp

    trace(A, N)


def main():
    trace(A, N)
    test(A, N)


if __name__ == "__main__":
    main()
