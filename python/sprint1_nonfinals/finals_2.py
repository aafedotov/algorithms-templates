# ID 68317816
def get_score(k: int, digits: list) -> int:
    """Финальное задание 15-го спринта. B) Ловкость рук."""

    frequency_dict = {}
    score = 0
    # считаем количество вхождений каждой цифры
    for digit in digits:
        if digit in frequency_dict:
            frequency_dict[digit] += 1
        else:
            frequency_dict[digit] = 1
    # считаем итоговую оценку, - это количество цифр, число вхождений которых
    # меньше или равно k
    for frequency in frequency_dict.values():
        if frequency <= k:
            score += 1

    return score


if __name__ == '__main__':

    required_quantity = int(input()) * 2
    keys = []
    for i in range(4):
        keys += [int(d) for d in input() if d.isdigit()]
    players_score = get_score(required_quantity, keys)
    print(players_score)
