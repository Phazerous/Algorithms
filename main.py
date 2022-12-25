def binary_search(list, item):
    low = 0
    high = len(list) - 1
    # steps = 0

    while low <= high:
        mid = (high + low) // 2
        guess = list[mid]
        steps += 1

        if item > guess:
            low = mid + 1
        elif item < guess:
            high = mid - 1
        else:
            # print(steps)
            return mid

    return None

random_list = list(range(1, 129)) # [1, 2, ..., 127, 128]
num = 24

print(binary_search(random_list, num))