def bigger(x, y):

    return int(x + y) > int(y + x)


def bubble(arr, n):

    for i in range(0, n):
        changes = 0
        for j in range(0, n - 1):
            if bigger(arr[j + 1], arr[j]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                changes += 1
        if changes == 0:
            break
    return arr


def main():

    n = int(input())
    arr = input().split()

    sorted_arr = bubble(arr, n)
    print(''.join(sorted_arr))


if __name__ == '__main__':

    main()
