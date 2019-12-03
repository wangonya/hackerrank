number_of_clouds = int(input())
cloud_types = list(map(int, input().split()))

counter = 0
ans = 0

while counter < number_of_clouds - 1:
    if counter + 2 >= number_of_clouds or cloud_types[counter + 2] == 1:
        # it's not possible to make two jumps if:
        # we're at the end of our list or:
        # making two jumps will land us at a 1
        counter += 1
        ans += 1
    else:
        counter += 2
        ans += 1
print(ans)
