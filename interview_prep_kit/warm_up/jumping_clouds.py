n = int(input())
clouds = list(map(int, input().split()))

counter = 0
answer = 0

while counter < n - 1:
    if counter + 2 >= n or clouds[counter + 2] == 1:
        # it's not possible to make two jumps if:
        # we're at the end of our list or:
        # making two jumps will land us at a 1
        counter += 1
        answer += 1
    else:
        counter += 2
        answer += 1
print(answer)
