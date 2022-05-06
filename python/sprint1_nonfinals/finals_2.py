# ID 68148637
def main():
    """Финальное задание 15-го спринта. B) Ловкость рук."""

    k = int(input()) * 2
    digits = []
    for i in range(4):
        digits += [int(d) for d in input() if d.isdigit()]
    frequency_dict = {}
    score = 0
    for digit in digits:
        if digit in frequency_dict:
            frequency_dict[digit] += 1
        else:
            frequency_dict[digit] = 1
    for frequency in frequency_dict.values():
        if frequency <= k:
            score += 1
    print(score)


if __name__ == '__main__':

    main()
