n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here

def bubble(arr):
    count_swap = 0
    for num in range(len(arr)-1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count_swap +=1
    return count_swap

print("Array is sorted in {} swaps.".format(bubble(a)))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
