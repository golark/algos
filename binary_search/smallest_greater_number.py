import math


# find smallest number in sequence that is greater than num
def smallest_greater_number(seq, num):

    start = 0
    end = len(seq) - 1
    min_diff = math.inf
    res = -1

    while start <= end:
        middle = (end - start) // 2 + start

        if seq[middle] > num and (seq[middle] - num) < min_diff:
            min_diff = seq[middle] - num
            res = seq[middle]

        if num > seq[middle]:
            start = middle+1
        else:
            end = middle-1
    return res


def main():
    seq = [4, 6, 8, 10, 20, 31]

    res = smallest_greater_number(seq, 11)

    print(f'smallest greater number = {res}')


if __name__ == "__main__":
    main()