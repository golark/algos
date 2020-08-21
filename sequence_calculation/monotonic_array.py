

# is_monotonic
# returns true if given sequence is monotonic ( all elements are in increasing or decreasing order )
# step 1 - check if expecting increasing/decreasing elements by comparing first and last elements
# step 2 - traverse through the sequence to determine if it is monotonic
# O(n) time, O(1) space
def is_monotonic(seq):

    if seq is None:
        return
    if len(seq) < 2:
        raise ValueError("length of sequence is less than 2")

    # step 1 - check if increasing or decreasing
    if seq[-1] > seq[0]:
        increasing = True
    else:
        increasing = False

    # step 2 - traverse and determine if the sequence is monotonic
    for i in range(len(seq)-1):

        if increasing and seq[i+1] < seq[i]:
            return False

        if (not increasing) and seq[i+1] > seq[i]:
            return False

    return True


def main():
    seq = [1,4,5,8,9,10,15,19]
    res = is_monotonic(seq)

    print(f'{res}')


if __name__ == "__main__":
    main()