def subseq(sub, seq):

    i = 0
    j = 0
    cnt = 0
    while i < len(sub) and j < len(seq):
        if sub[i] != seq[j]:
            j += 1
            continue
        i += 1
        j += 1
        cnt += 1

    return len(sub) == cnt


def main():

    s = input()
    t = input()
    print(subseq(s, t))


if __name__ == '__main__':

    main()
