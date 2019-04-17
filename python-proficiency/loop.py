# https://www.hackerrank.com/challenges/30-loops/problem


def loop(n):
    output = 1
    for output in range(10):
        output += 1
        print('{} x {} = {}'.format(n, output, n*output))


if __name__ == '__main__':
    n = int(input())
    loop(n)
