def binary_search(target_list, key):
    left = 0
    right = len(target_list)
    while left < right:
        mid = (left + right) // 2
        if target_list[mid] == key:
            return True
        elif key < target_list[mid]:
            right = mid
        else:
            left = mid + 1

    return False


N = int(input())
S = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))

count = 0
for key in T:
    if binary_search(S, key):
        count += 1

print(count)
