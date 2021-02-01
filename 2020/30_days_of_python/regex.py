import re

def list_search(data):
    r = re.compile(".*@gmail.com")
    output = list(sorted(filter(r.match, data)))

    for name in output:
        print(name.split()[0])

if __name__ == '__main__':
    N = int(input())
    data = list()

    for _ in range(N):
        d = input()
        data.append(d)

    list_search(data)
