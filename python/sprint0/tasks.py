def main():

    n = int(input())
    values = list(map(int, input().split()))
    result = 0
    if n == 1:
        result += 1
    else:
        if values[n - 1] > values[n - 2]:
            result += 1
        if values[0] > values[1]:
            result += 1
        for i in range(1, n - 1):
            if values[i] > values[i - 1] and values[i] > values[i + 1]:
                result += 1
    print(result)


if __name__ == '__main__':

    main()

# "Соседи"
# def main():
#
#     n = int(input())
#     m = int(input())
#     matrix = []
#     for i in range(n):
#         row = list(map(int, input().split()))
#         matrix.append(row)
#     row = int(input())
#     col = int(input())
#
#     result = []
#
#     if col < m - 1:
#         result.append(matrix[row][col+1])
#     if col > 0:
#         result.append(matrix[row][col-1])
#     if row > 0:
#         result.append(matrix[row-1][col])
#     if row < n - 1:
#         result.append(matrix[row+1][col])
#
#     result.sort()
#     print(' '.join(map(str, result)))
#
#
# if __name__ == '__main__':
#
#     main()


# "Чётные и нечётные числа"

# def main():
#
#     values = list(map(lambda k: int(k) % 2 == 0, input().split()))
#     if all(values) or not any(values):
#         print('WIN')
#     else:
#         print('FAIL')
#
#
# if __name__ == '__main__':
#
#     main()


# "Значения функции"

# def main():
#     values = list(map(int, input().split()))
#     result = values[0] * (values[1] ** 2) + values[2] * values[1] + values[3]
#     print(result)
#
#
# if __name__ == '__main__':
#
#     main()


# "Две фишки - 2 (добавление структуры данных)"

# N = int(input())
# arr = list(map(int, input().split()))
# K = int(input())
#
# previous = set()
# result = None
#
# for first in arr:
#     second = K - first
#     if second in previous:
#         result = str(first) + ' ' + str(second)
#         break
#     previous.add(first)
#
# print(result)


# "Две фишки - 2 (сортировка)"
#
# N = int(input())
# arr = list(map(int, input().split()))
# K = int(input())
#
# arr.sort()
#
# left = 0
# right = N - 1
# result = None
#
# while left < right:
#     current_sum = arr[left] + arr[right]
#     if current_sum == K:
#         result = str(arr[left]) + ' ' + str(arr[right])
#         break
#     if current_sum > K:
#         right -= 1
#     if current_sum < K:
#         left += 1
#
# print(result)


# "Две фишки"

# N = int(input())
# arr = list(map(int, input().split()))
# K = int(input())
#
# result = None
# for i in range(0, N):
#     if result:
#         break
#     for j in range(i + 1, N):
#         if arr[i] + arr[j] == K:
#             result = str(arr[i]) + ' ' + str(arr[j])
#             break
# print(result)


# "Скользящее среднее"

# N = int(input())
# arr = list(map(int, input().split()))
# K = int(input())
#
# result = []
# current_sum = sum(arr[0:K])
# result.append(current_sum / K)
#
# for i in range(N - K):
#     current_sum -= arr[i]
#     current_sum += arr[i + K]
#     result.append(current_sum / K)
#
# print(' '.join(map(str, result)))


# "Застежка-молния"

# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
#
# result = []
#
# for i in range(0, n):
#     result.append(a[i])
#     result.append(b[i])
#
# print(' '.join(map(str, result)))
