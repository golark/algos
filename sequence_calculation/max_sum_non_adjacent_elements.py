import math

# max_sum_non_adjacent_elements
# approach: first sort the array, then traverse backwards to find maximum sum
# warning: mutates input sequence
# O(nlogn) time and space O(1)
def max_sum_non_adjacent_elements(seq):

    # @todo check sequence length

    # step 1 - sort the sequence
    seq.sort(key=lambda x: x)

    # step 2 - traverse backwards and find maxsum
    max_sum = -math.inf
    p = len(seq)-1
    s = 0
    while p >= 0:
        s = s + seq[p]
        if s > max_sum:
            max_sum = s
        p = p - 2

    p = len(seq) - 2
    s = 0
    while p >= 0:
        s = s + seq[p]
        if s > max_sum:
            max_sum = s
        p = p - 2

    return max_sum


def main():
    seq = [1,4,-9,5,8,9,10,15,19]
    res = max_sum_non_adjacent_elements(seq)

    print(f'{res}')


if __name__ == "__main__":
    main()
