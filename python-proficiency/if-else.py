# https://www.hackerrank.com/challenges/py-if-else/problem


def check_weird(n):
    if (not n % 2 == 0) or (n % 2 == 0 and n in range(6, 21)):
        solution = print("Weird")
        return solution
    if (n % 2 == 0) or (n % 2 == 0 and n > 20):
        solution = print("Not Weird")
        return solution


if __name__ == '__main__':
    n = int(input())
    check_weird(n)
