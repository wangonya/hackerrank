steps = int(input())
path = input()

level = 0
valleys = 0

for step in path:
    if step == 'U':
        level += 1
        # we're only interested in sequences coming from 'U' into 0
        # because they represent coming from a valley into level ground
        if level == 0:
            valleys += 1
    else:
        level -= 1

print(valleys)
