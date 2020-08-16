import heapq


# k_closest_numbers
# find k closest numbers to X
# X might not be in the sequence
def k_closest_numbers(seq, k, X):

    # step 1- find difference sequence
    diff_seq = []
    for i in seq:
        diff_seq.append(abs(i - X))

    # step 2 - min heap based algorithm to find minimum in difference sequence
    # add k elements to heap
    min_heap  = []
    for i in range(len(seq)):
        heapq.heappush(min_heap, -diff_seq[i])

    # traverse through sequence to find closer numbers
    for i in range(i, len(diff_seq)):
        if -diff_seq[i] > max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -diff_seq[i])
            idx[i] = 1

    # step 3 - add numbers to X to prune the results ( remove difference )
    return [X+i for i in max_heap]


def main():
    seq = [10,6,3,1,0,19,18,2]

    res = k_closest_numbers(seq, 3, 6)
    print(f'{res}')


if __name__ == "__main__":
    main()