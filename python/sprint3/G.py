def counting_sort(n, arr):

    colors = [0, 0, 0]
    sorted_arr = []
    for value in arr:
        colors[value] += 1

    for color, value in enumerate(colors):
        sorted_arr.extend([color for i in range(value)])

    return sorted_arr


def main():

    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = counting_sort(n, arr)
    print(' '.join(list(map(str, sorted_arr))))


if __name__ == '__main__':

    main()
