# https://www.hackerrank.com/challenges/python-mod-divmod/problem


def solution(n, x):
    print(n//x)
    print(n % x)
    print(divmod(n, x))


if __name__ == "__main__":
    n = int(input())
    x = int(input())
    solution(n, x)
