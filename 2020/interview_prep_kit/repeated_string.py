string = input()
n = int(input())

if not string.count('a'):
    # edge case: no 'a's in string
    print(0)
elif len(set(string)) == 1:
    # the string is all 'a's so return `n`
    print(n)
else:
    a = string.count('a')
    # number of groups of the original string in the repeated string
    g = n // len(string)
    # if the group doesn't fit perfectly, get the remainder
    r = n % len(string)
    count = a * g + string[:r].count('a')
    print(count)
