def is_correct_bracket_seq(seq):

    if not seq:
        return True

    brackets = {'(': 0}
    last_open_brackets = []

    for bracket in seq:

        if bracket == '(':
            brackets['('] += 1
            last_open_brackets.append('(')
        if bracket == ')':
            if not last_open_brackets or last_open_brackets[-1] != '(':
                return False
            last_open_brackets.pop()
            brackets['('] -= 1

    return not any(brackets.values())


def psp(n, prefix):

    if n == 0:
        if is_correct_bracket_seq(prefix):
            print(prefix)
    else:
        psp(n - 1, prefix + '(')
        psp(n - 1, prefix + ')')


def main():

    n = int(input())
    psp(2 * n, '')


if __name__ == '__main__':

    main()
