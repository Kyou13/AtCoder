import sys
N,M = map(int, input().split())
a = [int(input()) for _ in range(M)]
if N == 1:
  print(1)
  sys.exit()
for i in range(1,len(a)):
  if a[i] - a[i-1] == 1:
    print(0)
    sys.exit()

dp = [[-9999 for i in range(N+1)] for j in range(3)]
dp[1] = [1 for i in range(N+1)]
dp[2][1] = 0
dp[2][2] = 2

for i in range(2,N):
  if i in a:
    dp[2][i+1] = dp[2][i-1]
  else:
    dp[2][i+1] = dp[2][i]*2-1
print(dp)
print(dp[2][N] % 1000000007)
