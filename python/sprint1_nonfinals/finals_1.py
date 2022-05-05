def get_min_distance(value, indexes):

    right = len(indexes) - 1
    if value < indexes[0]:
        return indexes[0]
    if value > indexes[right]:
        return indexes[right]

    left = 0
    closer = left
    while left <= right:
        mid = left + (right - left) // 2
        if value > indexes[mid]:
            left = mid + 1
        else:
            right = mid - 1
        if abs(indexes[mid] - value) < abs(indexes[closer] - value):
            closer = mid
    return abs(value - indexes[closer])





def main():

    n = int(input())
    numbers = list(map(int, list(input().split())))
    null_indexes = []
    null_distances = []
    for i in range(0, n):
        if numbers[i] == 0:
            null_indexes.append(i)
    for i in range(0, n):
        if numbers[i] == 0:
            null_distances.append(0)
        else:
            min_distance = get_min_distance(i, null_indexes)
            null_distances.append(min_distance)

    print(' '.join(map(str, null_distances)))


if __name__ == '__main__':

    main()
