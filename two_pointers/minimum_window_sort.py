

# minimum_window_sort
# length of the smallest subsequence, when sorted will sort the whole array
# two pointers approach
# O(n) time complexity, O(1) space
# step 1 - traverse back/forth from each end of the sequence to find sorted part of the sequence
def minimum_window_sort(seq):

    if seq is None:
        return

    ascending = seq[-1] > seq[0]

    p = 0
    q = len(seq)-1
    while p < q:

        if ascending:
            if seq[p] > seq[p+1] and seq[q] < seq[q-1]:
                return seq[p:q+1]

            if seq[p+1] >= seq[p]:
                p = p + 1
            if seq[q-1] <= seq[q]:
                q = q - 1
        else:
            if seq[p] < seq[p+1] and seq[q] > seq[q-1]:
                return seq[p:q+1]

            if seq[p+1] <= seq[p]:
                p = p + 1
            if seq[q-1] >= seq[q]:
                q = q - 1

    return seq[p:q+1]


def main():
    seq = [1, 2, 5, 3, 7, 10, 9, 12]
    res = minimum_window_sort(seq)
    print(f'{res}')

    seq2 = [1, 2, 3, 5, 8, 7, 9, 12]
    res = minimum_window_sort(seq2)
    print(f'{res}')

    seq3 = [1, 2, 3, 5, 7, 7, 9, 12]
    res = minimum_window_sort(seq3)
    print(f'{res}')

    seq4 = [12,11,9,3,4,1]
    res = minimum_window_sort(seq4)
    print(f'{res}')


if __name__ == "__main__":
    main()