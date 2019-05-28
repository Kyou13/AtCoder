N = int(input())
X = []
for i in range(N):
  S, P = input().split()
  P = int(P)
  X.append([S,P,i+1])
X = sorted(X,key=lambda x:x[1],reverse=True)
X = sorted(X,key=lambda x:x[0])

for i in range(N):
  print(X[i][2])
