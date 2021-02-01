# https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem

try:
    s = int(input())
    print(s)
except ValueError:
    print('Bad String')
