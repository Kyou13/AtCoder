import math
A,B,T = map(int, input().split())
result = math.floor(T/A) * B
print(result)
