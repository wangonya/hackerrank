returned = list(map(int, input().strip().split()))
expected = list(map(int, input().strip().split()))

check_day = returned[0] - expected[0]
check_month = returned[1] - expected[1]
check_year = returned[2] - expected[2]

if (check_day > 0) and (check_month <= 0) and (check_year <= 0):
    print(check_day*15)
elif (check_month > 0) and (check_day <= 0) and (check_year <= 0):
    print(check_month*500)
elif (check_year) > 0:
    print(1000)
else:
    print(0)
