
# dutch_national_flag
# sort in place, array consisting items 0,1,2
# two pointers approach
# traverse through the sequence keeping to references to 0s and 2s at the beginnig/end of the sequence
# move 0s and 2s only to beginning/end, keeping 1s in the middle
# O(n) time, O(1) space
def dutch_national_flag(seq):

    if seq is None:
        return
    if len(seq) < 2:
        return

    p = 0
    q = len(seq)-1

    # move p/q to the end of 0,2 series
    while seq[p] == 0:
        p = p + 1
    while seq[q] == 2:
        q = q - 1

    r = range(p+1, q+1)
    for i in r:

        if seq[i] == 0:
            seq[p], seq[i] = seq[i], seq[p]
            p = p + 1
        elif seq[i] == 2:
            seq[q], seq[i] = seq[i], seq[q]
            q = q - 1

        print(f'{seq}')



def main():
    seq = [1, 0, 2, 1, 0]
    dutch_national_flag(seq)
    print(f'{seq}')


if __name__ == "__main__":
    main()