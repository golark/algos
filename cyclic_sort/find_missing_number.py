

# find missing number in sequence 0 - n
def find_missing_number(seq):
    missing = 0

    # step 1 - sort the items using cyclic sort
    for i in range(len(seq)):
        if seq[i] < len(seq) and seq[seq[i]] != seq[i]:
            # swap
            seq[seq[i]], seq[i] = seq[i], seq[seq[i]]

    print(f'{seq}')
    # step 2 - find missing item in sorted list
    for i in range(len(seq)):
        if i != seq[i]:
            return i
    return -1

def main():
    seq = [5,0,1,2,3]
    missing = find_missing_number(seq)

    print(f'missing = {missing}')


if __name__ == "__main__":
    main()
