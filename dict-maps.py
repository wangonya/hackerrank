phonebook = {}
entries = int(input())

for _ in range(entries):
    name, num = input().strip().split()
    name, num = [str(name), int(num)]
    phonebook[name] = num

while True:
    try:
        search = str(input())
        if search in phonebook:
            print('{}={}'.format(search, phonebook[search]))
        else:
            print('Not found')
    except EOFError:
        break
