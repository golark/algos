

# strings_with_backspaces
# given strings with backspace character '#'
# check if they are equal
def strings_with_backspaces(str1, str2):

    p = len(str1)-1
    q = len(str2)-1

    while p >= 0 and q >= 0:
        # handle backspace character
        if str1[p] == '#':
            p = p - 2
        if str2[q] == '#':
            q = q - 2

        # compare characters
        if p >= 0 and q >= 0:
            if str1[p] != str2[q]:
                return False
        else:
            return False

        p = p - 1
        q = q - 1

    # p must equal q for, string equality
    return p == q


def main():
    str1 = "xy#z"
    str2 = "xzz#"

    res = strings_with_backspaces(str1, str2)
    print(f'{res}')


if __name__ == "__main__":
    main()