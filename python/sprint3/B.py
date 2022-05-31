KEYS_CHARS = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def combi(n, keys, prefix):
    if n == 0:
        print(prefix + ' ', end='')
    else:
        for char in KEYS_CHARS[keys[n - 1]]:
            combi(n - 1, keys, prefix + char)


def main():
    keys = input()[::-1]
    keys = [int(i) for i in keys]
    n = len(keys)
    combi(n, keys, '')


if __name__ == '__main__':

    main()
