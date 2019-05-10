X = int(input())
max = 0
for i in range(2,X):
    b = 2
    tmp = i**b
    while tmp <= X:
        if tmp>max:
            max = tmp
        b += 1
        tmp = i**b
if max == 0:
    max = 1

print(max)
