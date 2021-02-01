s = input()
n = int(input())

if not s.count('a'):
    # edge case - no 'a's in string
    print(0)
elif len(set(s)) == 1:
    # the string is all 'a's
    print(n)
else:
    a = s.count('a')
    # find number of groups of the original str in
    # the repeated str
    g = n // len(s)
    # if the group doesn't fit perfectly get the remainder
    r = n % len(s)
    count = a * g + s[:r].count('a')
    print(count)
