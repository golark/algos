import math


def smallest_greater_letter(seq, letter):

    start = 0
    end = len(seq) - 1
    min_diff = math.inf
    res = ' '

    while start <= end:
        middle = (end - start) // 2 + start

        print(f'{ord(seq[middle]) - ord(letter)}')

        if ord(seq[middle]) > ord(letter) and (ord(seq[middle]) - ord(letter)) < min_diff:
            min_diff = ord(seq[middle]) - ord(letter)
            res = seq[middle]

        if ord(letter) > ord(seq[middle]):
            start = middle+1
        else:
            end = middle-1
    return res


def main():
    seq = ['a', 'c', 'f', 'h']

    res = smallest_greater_letter(seq, 'f')

    print(f'smallest greater letter = {res}')

if __name__ == "__main__":
    main()