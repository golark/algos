

# find missing number in sequence 1 - n
def find_all_missing_numbers(seq):

    missing = []

    # step 1 - sort the sequence
    for i in range(len(seq)):
        num = seq[i]
        if seq[num-1] != num:
            # swap
            seq[i], seq[num-1] = seq[num-1], seq[i]

    # step 2 - find missing numbers
    for i in range(len(seq)):
        if seq[i] != i+1:
            missing.append(i+1)
    return missing


def main():
    seq = [2, 3, 1, 8, 2, 3, 5, 1]
    missing = find_all_missing_numbers(seq)

    print(f'missing = {missing}')


if __name__ == "__main__":
    main()
