# ID 68317697
def nearest_zero(n: int, numbers: list) -> list:
    """Финальное задание 15-го спринта. А) Ближайший ноль."""

    # формируем список с индексами всех нулей
    null_indexes = [i for i in range(0, n) if numbers[i] == 0]
    null_amount = len(null_indexes)
    null_distances = []
    current_null = 0
    # флаг для первого нуля, если True - мы не переходим к следующему нулю
    is_first_null = True
    for i, number in enumerate(numbers):
        # если встречается ноль, добавляем 0 в результирующий список,
        # обновляем итератор current_null
        if number == 0:
            null_distances.append(0)
            if current_null == 0 and is_first_null:
                is_first_null = False
            else:
                current_null += 1
        else:
            # пока ноль не последний - мы выбираем между двух соседних нулей,
            # который ближе
            if current_null != null_amount - 1:
                min_distance = min(
                    abs(null_indexes[current_null] - i),
                    abs(null_indexes[current_null + 1] - i)
                )
                null_distances.append(min_distance)
            else:
                null_distances.append(abs(null_indexes[current_null] - i))

    return null_distances


if __name__ == '__main__':

    amount = int(input())
    houses = list(map(int, list(input().split())))
    distances_to_vacant_lot = nearest_zero(amount, houses)
    to_print = ' '.join(map(str, distances_to_vacant_lot))
    print(to_print)
