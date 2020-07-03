# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are

import itertools


def sock_merchant(socks):
    print(socks)
    # sort socks
    # python sort function is O(n log n)
    # so use it instead of writing your own function
    socks = sorted(socks)
    print(socks)

    # use itertools to group together matches
    grouped_socks = [list(s) for _, s in itertools.groupby(socks)]
    print(grouped_socks)

    pairs = 0

    for group in grouped_socks:
        pairs += len(group) // 2

    print(pairs)


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    sock_merchant(ar)
