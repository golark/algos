import heapq


# k_closest_numbers
# find k closest numbers to X
# X might not be in the sequence
def k_closest_numbers(seq, k, X):

    # step 1- find difference sequence
    diff_seq = []
    for i in seq:
        diff_seq.append(i - X)

    # step 2 - min heap based algorithm to find minimum in difference sequence
    # add k elements to heap
    min_heap = []
    for i in range(len(seq)):
        t = (abs(diff_seq[i]), seq[i])
        heapq.heappush(min_heap, t)

    # step 3 - add numbers to X to prune the results ( remove difference )
    print(f'{min_heap}')

    return [a for (_, a) in min_heap[0:k]]


def main():
    seq = [10,6,5,7,1,0,19,18,2]

    res = k_closest_numbers(seq, 3, 6)
    print(f'{res}')


if __name__ == "__main__":
    main()