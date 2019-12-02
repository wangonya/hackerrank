def counting_valleys(path):
    print(path)
    step_counter = 0
    in_valley_counter = 0
    for c in path:
        if c == 'U':
            step_counter += 1
        elif c == 'D':
            step_counter -= 1

        if step_counter < 0:
            pass
        elif step_counter > 0:
            in_valley_counter += 1

    return in_valley_counter


if __name__ == "__main__":
    steps = int(input())
    path = input()

    # slices path into number of steps incase extra was entered
    path = path[0:steps]

    print(counting_valleys(path))
