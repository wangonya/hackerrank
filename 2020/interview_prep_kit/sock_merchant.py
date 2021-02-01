import itertools


def sock_merchant(sock_list):
    """Uses itertools to group together similar values,
    then counts the number of pairs in the groups."""
    grouped_sock_list = [
        list(g) for _, g in itertools.groupby(sorted(sock_list))
    ]

    total_pairs = 0

    for group in grouped_sock_list:
        pairs = len(group) // 2
        total_pairs += pairs

    return total_pairs


if __name__ == '__main__':
    n = int(input())
    list_ = list(map(int, input().rstrip().split()))

    print(sock_merchant(list_))
