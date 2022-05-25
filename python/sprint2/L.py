if __name__ == '__main__':

    n, m = map(int, input().split())
    k = 10 ** m
    if n <= 1:
        print(1)
    else:
        previous, current = 0, 1
        for i in range(2, n + 2):
            previous, current = current, (previous + current) % k
        print(current)
