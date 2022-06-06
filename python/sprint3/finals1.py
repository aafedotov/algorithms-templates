def array_recovery(arr, n):

    recovered_array = []
    i = 0
    while i < n - 1:
        if arr[i] > arr[i + 1]:
            break
        i += 1
    recovered_array.extend(arr[i + 1: n])
    recovered_array.extend(arr[0: i + 1])
    return recovered_array, i


def binary_search(arr, n, k):

    mid = n // 2
    left = 0
    right = n - 1

    while arr[mid] != k and left <= right:

        if k > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2

    if left > right:
        return 'Искомое значение не найдено'

    return mid


def broken_search(nums: list, target: int) -> int:

    n = len(nums)
    recovered, index = array_recovery(nums, n)
    binary_index = binary_search(recovered, n, target)
    if binary_index >= index + 1:
        return binary_index - index - 2
    return binary_index + index + 1


def main():

    n = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    print(broken_search(arr, k))


if __name__ == '__main__':

    main()

