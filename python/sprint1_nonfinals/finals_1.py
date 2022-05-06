# ID 68147413
def main():
    """Финальное задание 15-го спринта. А) Ближайший ноль."""

    n = int(input())
    numbers = list(map(int, list(input().split())))
    null_indexes = [i for i in range(0, n) if numbers[i] == 0] # формируем список с индексами всех нулей
    null_amount = len(null_indexes)
    null_distances = []
    current_null = 0
    is_first_null = True # флаг для первого нуля, если True - мы не переходим к следующему индексу нуля
    for i, number in enumerate(numbers):
        if number == 0: # если встречается ноль, добавляем 0 в результирующий список, обновляем итератор current_null
            null_distances.append(0)
            if current_null == 0 and is_first_null:
                is_first_null = False
            else:
                current_null += 1
        else:
            if current_null != null_amount - 1:
                min_distance = min(
                    abs(null_indexes[current_null] - i),
                    abs(null_indexes[current_null + 1] - i)
                ) # пока ноль не последний - мы выбираем между двух соседних нулей, который ближе
                null_distances.append(min_distance)
            else:
                null_distances.append(abs(null_indexes[current_null] - i))

    print(' '.join(map(str, null_distances)))


if __name__ == '__main__':

    main()
