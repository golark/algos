

# given a target determine pairs that sum up to the target
# input sequence is unsorted
def target_sum(seq, target):
    pairs = []

    # keep a hash map of sequence item difference from target
    diff_map = {}
    for i in range(len(seq)):

        # check if difference exits in diff map
        if seq[i] in diff_map:
            pairs.append([ target-seq[i], seq[i]])
        else:  # otherwise add to diff map
            diff_map[target - seq[i]] = 1

    return pairs


def main():
    seq = [1,5,4,2,3,0,6]
    res = target_sum(seq, 5)

    print(f'{res}')


if __name__ == "__main__":
    main()