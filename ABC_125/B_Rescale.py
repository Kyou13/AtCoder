import numpy as np
N = int(input())
V = np.array(list(map(int, input().split())))
C = np.array(list(map(int, input().split())))

diff = V-C
result = diff[diff>0].sum()
print(result)
