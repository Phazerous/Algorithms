def find_max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print(find_max([5, 4, 3, 424, 24, 2,134, 564, 349]))