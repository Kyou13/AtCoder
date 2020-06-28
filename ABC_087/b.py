A = int(input())
B = int(input())
C = int(input())
X = int(input())

count = 0
for a in range(0, A+1):
    for b in range(0, B+1):
        for c in range(0, C+1):
            if X == a*500+b*100+c*50:
                count += 1

print(count)
