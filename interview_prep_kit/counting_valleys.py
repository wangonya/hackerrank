def counting_valleys(path):
    print(path)


if __name__ == "__main__":
    steps = int(input())
    path = input()

    # slices path into number of steps incase extra was entered
    path = path[0:steps]

    # converts step letters into 1s and 0s for easier computation
    path = path.replace("U", "1")
    path = path.replace("D", "0")

    counting_valleys(path)
