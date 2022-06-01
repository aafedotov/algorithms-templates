def bubble(arr, n):

    for i in range(0, n):
        changes = 0
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                changes += 1
        if changes == 0:
            if i == 0:
                print(' '.join(map(str, arr)))
            break
        print(' '.join(map(str, arr)))


def main():

    n = int(input())
    arr = list(map(int, input().split()))
    bubble(arr, n)


if __name__ == '__main__':

    main()
