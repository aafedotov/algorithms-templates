def flowers(n, dots):

    result = []
    dots = sorted(dots, key=lambda k: k[0])
    for dot in dots:
        if not result:
            result.append(dot)
            continue
        current = result.pop()
        if current == dot:
            result.append(dot)
            continue
        if dot[1] < current[1]:
            result.append(current)
            continue
        if dot[0] <= current[1]:
            result.append([current[0], dot[1]])
            continue
        result.append(current)
        result.append(dot)

    return result


def main():

    n = int(input())
    dots = []
    for i in range(0, n):
        dots.append(list(map(int, input().split())))
    result = flowers(n, dots)
    for item in result:
        print(' '.join(map(str, item)))


if __name__ == '__main__':

    main()
