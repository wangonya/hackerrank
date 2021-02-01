# https://www.hackerrank.com/challenges/30-2d-arrays/problem

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    res = []

    for x in range(0, 4):
        for y in range(0, 4):
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            # print('first sum array ==> {}'.format(arr[x][y:y+3]))
            # print('2 sum array ==> {}'.format(arr[x+1][y+1]))
            # print('3 sum array ==> {}'.format(arr[x+2][y:y+3]))
            res.append(s)

    print(max(res))
