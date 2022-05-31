def found_day(arr, left, right, s):

    mid = (left + right) // 2
    if left >= right:
        return left
    if arr[mid] > s:
        right = mid
        return found_day(arr, left, right, s)
    elif arr[mid] < s:
        left = mid + 1
        return found_day(arr, left, right, s)
    elif arr[mid] == s:
        return mid


def main():

    n = int(input())
    days_income = list(map(int, input().split()))
    price = int(input())
    if price > days_income[n - 1]:
        x = -1
    else:
        x = found_day(days_income, 0, n, price)
        while x > 0:
            if days_income[x] != days_income[x - 1]:
                break
            x -= 1
        x += 1
    if price * 2 > days_income[n - 1]:
        y = -1
    else:
        y = found_day(days_income, 0, n, price * 2)
        while y > 0:
            if days_income[y] != days_income[y - 1]:
                break
            y -= 1
        y += 1
    print(x, y)


if __name__ == '__main__':

    main()
