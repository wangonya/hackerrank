import math

n = int(input())
output = []

for _ in range(n):
    i = int(input())
    if i > 1:
        for x in range(2, int(math.sqrt(i))+1):
            if (i % x) == 0:
                output.append("Not prime")
                break
        else:
            output.append("Prime")
    else:
        output.append("Not prime")

print(*output, sep='\n')
