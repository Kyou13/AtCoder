import sys
antenna = [int(input()) for _ in range(5)]
k = int(input())
for index, i in enumerate(antenna[:-1]):
  for j in antenna[index+1:]:
    if j-i>k:
      print(':(')
      sys.exit()
print("Yay!")
