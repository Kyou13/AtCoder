from itertools import permutations
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

permutations_N = list(permutations(range(1, N+1)))
a = permutations_N.index(P)
b = permutations_N.index(Q)
print(abs(a-b))
