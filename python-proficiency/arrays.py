# https://www.hackerrank.com/challenges/30-arrays/problem


def solution(arr):
    r = list(reversed(arr))
    print(*r, sep=' ')


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))[:n]
    solution(arr)
