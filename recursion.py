# https://www.hackerrank.com/challenges/30-recursion/problem


def factorial(n):
    return 1 if (n < 1) else n * factorial(n-1)


if __name__ == "__main__":
    n = int(input())
    print(factorial(n))
