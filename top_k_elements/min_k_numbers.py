import heapq


def min_k_numbers(seq, k):
    max_heap = []

    for i in range(k):
        heapq.heappush(max_heap, -seq[i])

    for i in range(k, len(seq)):
        if -seq[i] > max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -seq[i])

    return [-i for i in max_heap]


def min_k_numbers2(seq, k):
    min_heap = []

    for i in seq:
        heapq.heappush(min_heap, i)

    return min_heap[0:k]


def main():

    seq = [1,4,5,10,0,1,2,5,2,15,19,21]
    res1 = min_k_numbers(seq, 3)
    res2 = min_k_numbers2(seq, 3)

    print(f'{res1}{res2`}')

if __name__ == "__main__":
    main()