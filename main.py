def sum_count(arr: list[int]):
    sum = 0
    count = 0
    for a in arr:
        if a > 0 and a % 2 == 0:
            count += 1
            sum += a
    return count, sum


if __name__ == '__main__':
    l = [1, 3, 4, -2]
    sum_count(l)
