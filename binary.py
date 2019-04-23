# https://www.hackerrank.com/challenges/30-binary-numbers/problem


def solution(binary):
    print(len(max(binary.split('0'))))


if __name__ == "__main__":
    n = int(input())
    binary = '{0:b}'.format(n)
    solution(str(binary))
