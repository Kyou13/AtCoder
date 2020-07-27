def binary_search(target_list, key):
    left = 0
    right = len(target_list)
    while left < right:
        mid = (left + right) // 2
        if target_list[mid] == key:
            return 0
        elif key < target_list[mid]:
            right = mid
        else:
            left = mid + 1

    left -= 1
    return key - target_list[left] if key - target_list[left] < target_list[right] - key else target_list[right] - key


distance = int(input())
n = int(input())
m = int(input())
d = [int(input()) for _ in range(n-1)]
k = [int(input()) for _ in range(m)]

d.extend([0, distance])
d.sort()

result = 0
for i in k:
    result += binary_search(d, i)
print(result)

