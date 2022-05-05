# "Лишняя буква"

# def main():
#
#     s1 = input()
#     s2 = input()
#     for char in s1:
#         s2 = s2.replace(char, '', 1)
#     print(s2)
#
#
# if __name__ == '__main__':
#
#     main()


# "Списочная форма"

# def main():
#
#     n = int(input())
#     a = int(input().replace(' ', ''))
#
#     b = int(input())
#     result = str(a + b)
#     for char in result:
#         print(f'{char} ')
#
#
# if __name__ == '__main__':
#
#     main()

# "Факторизация"

# def main():
#
#     n = int(input())
#     # simple = []
#     # not_simple = []
#     # for i in range(2, n + 1):
#     #     if i not in not_simple:
#     #         simple.append(i)
#     #     not_simple += [number for number in range(i * i, n + 1, i)]
#
#     remainder = n
#     i = 2
#     deviders = []
#
#     while i * i <= n:
#         if remainder % i == 0:
#             deviders.append(i)
#             remainder = remainder / i
#         else:
#             i += 1
#     if remainder > 1:
#         deviders.append(int(remainder))
#     print(' '.join(map(str, deviders)))
#
#
# if __name__ == '__main__':
#
#     main()


# "Степень четырех"

# import math
#
#
# def main():
#
#     number = int(input())
#     log_4 = math.log(number, 4)
#     result = int(log_4) == log_4
#     print(result)
#
#
# if __name__ == '__main__':
#
#     main()


# "Двоичная система"

# def main():
#
#     a = list(map(int, list(input())))
#     b = list(map(int, list(input())))
#     dif = len(a) - len(b)
#     if dif > 0:
#         b = [0] * dif + b
#     if dif < 0:
#         a = [0] * abs(dif) + a
#     a.reverse()
#     b.reverse()
#     overflow = 0
#     c = []
#     for i in range(0, len(a)):
#         if overflow == 0:
#             if a[i] + b[i] == 0:
#                 c.append(0)
#             elif a[i] + b[i] == 1:
#                 c.append(1)
#             else:
#                 c.append(0)
#                 overflow = 1
#         else:
#             if a[i] + b[i] == 0:
#                 c.append(1)
#                 overflow = 0
#             elif a[i] + b[i] == 1:
#                 c.append(0)
#                 overflow = 1
#             else:
#                 c.append(1)
#                 overflow = 1
#     if overflow == 1:
#         c.append(1)
#     c.reverse()
#     print(''.join(map(str, c)))
#
#
# if __name__ == '__main__':
#
#     main()


# "Работа из дома"

# def main():
#
#     number = int(input())
#     result = ''
#     current_remainder = number
#     while current_remainder >= 2:
#         result += str(current_remainder % 2)
#         current_remainder = current_remainder // 2
#     result += str(current_remainder)
#     print(result[::-1])
#
#
# if __name__ == '__main__':
#
#     main()


# "Палиндром"

# def main():
#
#     text = input()
#     cleared_text = ''.join(
#         char for char in text if char.isalpha() or char.isalnum()
#     ).lower()
#     result = cleared_text == cleared_text[::-1]
#     print(result)
#
#
# if __name__ == '__main__':
#
#     main()


# "Самое длинное слово"

# def main():
#
#     l = int(input())
#     text = list(input().split())
#     max_length = 0
#     max_word = ''
#
#     for word in text:
#         current_len = len(word)
#         if current_len > max_length:
#             max_length = current_len
#             max_word = word
#
#     print(max_word)
#     print(max_length)


# if __name__ == '__main__':
#
#     main()


# "Хаотичность погоды"

# def main():
#
#     n = int(input())
#     values = list(map(int, input().split()))
#     result = 0
#     if n == 1:
#         result += 1
#     else:
#         if values[n - 1] > values[n - 2]:
#             result += 1
#         if values[0] > values[1]:
#             result += 1
#         for i in range(1, n - 1):
#             if values[i] > values[i - 1] and values[i] > values[i + 1]:
#                 result += 1
#     print(result)
#
#
# if __name__ == '__main__':
#
#     main()

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
