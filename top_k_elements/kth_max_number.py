import heapq

# kth_max_number
# heap based implementation
def kth_max_number(seq, k):
    r = 0
    min_heap = []

    if k > len(seq):
        raise IndexError("k is smaller than the length of the sequence")

    # add k elements to the heap
    for i in range(k):
        heapq.heappush(min_heap, seq[i])

    # parse the sequence and add any new max
    for i in range(k, len(seq)):
        if seq[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, seq[i])

    return min_heap[0]


def main():

    seq = [10,6,3,1,0,19,18,2]

    res = kth_max_number(seq, 3)
    print(f'{res}')


if __name__ == "__main__":
    main()
