# https://www.hackerrank.com/challenges/30-review-loop/problem
# https://stackoverflow.com/questions/509211/understanding-slice-notation


def solution(words):
    for word in words:
        print('{} {}'.format(word[::2], word[1::2]))


if __name__ == "__main__":
    n = int(input())
    limit = 0
    words = []
    while limit in range(n):
        s = str(input())
        words.append(s)
        limit += 1
    solution(words)
