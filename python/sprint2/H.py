def is_correct_bracket_seq(seq):
    
    if not seq:
        return True

    brackets = {'(': 0, '[': 0, '{': 0}
    last_open_brackets = []

    for bracket in seq:

        if bracket == '(':
            brackets['('] += 1
            last_open_brackets.append('(')
        if bracket == '[':
            brackets['['] += 1
            last_open_brackets.append('[')
        if bracket == '{':
            brackets['{'] += 1
            last_open_brackets.append('{')

        if bracket == ')':
            if not last_open_brackets or last_open_brackets[-1] != '(':
                return False
            last_open_brackets.pop()
            brackets['('] -= 1
        if bracket == ']':
            if not last_open_brackets or last_open_brackets[-1] != '[':
                return False
            brackets['['] -= 1
            last_open_brackets.pop()
        if bracket == '}':
            if not last_open_brackets or last_open_brackets[-1] != '{':
                return False
            brackets['{'] -= 1
            last_open_brackets.pop()

    return not any(brackets.values())


def main():

    seq = input()
    print(is_correct_bracket_seq(seq))


if __name__ == '__main__':

    main()
