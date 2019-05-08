returned = list(map(int, input().strip().split()))
expected = list(map(int, input().strip().split()))

fine = 0

if returned[2] > expected[2]:
    fine = 10000
elif returned[2] == expected[2]:
    if returned[1] > expected[1]:
        fine = (returned[1] - expected[1])*500
    elif returned[1] == expected[1]:
        if returned[0] > expected[0]:
            fine = (returned[0] - expected[0])*15

print(fine)
