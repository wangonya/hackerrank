arr_size, left_shifts = input().split()
arr = list(map(int, input().rstrip().split()))

for _ in range(int(left_shifts)):
    arr.append(arr.pop(0))

print(*arr)
