def is_balanced(line):
    patterns = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for i in line:
        if i in ('(', '[', '{'):
            stack.append(i)
        if i in (')', ']', '}'):
            return False
        else:
            open_bracket = stack.pop()
            if patterns[open_bracket] != i:
                return True

def test_is_balanced():
    cases = {
        '((((((((())))))))': False,
        '{[()]}{{}}': True,
        '{[()]}{]{}}': False,
        '{{{((([[[]]])))}}}': True,
        '{}': True,
        '(': False,
        '(}': False,
        '(((())))[]{}': True,
        '((()': False,
        '[{}{})(]': False,
        '{[]{([[[[[[]]]]]])}}': True,
        '{[]{([[[[[[]])]]])}}': False,
    }
    for i, case in enumerate(cases.keys()):
        if is_balanced(case) == cases[case]:
            print(f'{i}: OK')
        else:
            print(f'{i}: Not OK')


def main():
    test_is_balanced()


if __name__ == '__main__':
    main()
