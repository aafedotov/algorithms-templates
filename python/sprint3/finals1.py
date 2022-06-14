# ID: 68950776
def broken_search(nums: list, target: int) -> int:
    """Бинарный поиск в отсортированном массиве со смещением."""

    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid + 1
    return -1


def main():

    k = int(input())
    arr = list(map(int, input().split()))
    print(broken_search(arr, k))


if __name__ == '__main__':

    main()
