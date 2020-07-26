N = int(input())
A = list(map(int, input().split()))

# current_money = 1000
# for i in range(N-1):
#     stock = 0
#     if A[i] < A[i+1]:
#         stock = current_money // A[i]
#     current_money += (A[i+1] - A[i]) * stock

# print(current_money)

dp = [1000] * (N)

# start_idx: 0
for i in range(1, N):
    dp[i] = dp[i-1]
    for j in range(i):
        V = dp[j] // A[j]
        W = dp[j] + (A[i] - A[j]) * V
        print(V, W)
        dp[i] = max(dp[i], W)

print(dp)
print(dp[-1])
