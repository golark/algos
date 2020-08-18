

# return the index of the item if in the sequence
# otherwise return -1
def search_for_number(seq, num):

    start = 0
    end = len(seq) - 1

    while start <= end:
        middle = (end - start) // 2 + start

        if num == seq[middle]:
            return middle
        if num > seq[middle]:
            start = middle+1
        else:
            end = middle-1
    return -1


def main():
    seq = [4, 6, 8, 10, 20, 31]

    res = search_for_number(seq, 10)

    print(f'key index = {res}')


if __name__ == "__main__":
    main()