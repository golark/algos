import heapq


# top_k_frequent_numbers
def top_k_frequent_numbers(seq, k):

    if len(seq) < k:
        raise IndexError("k is less than the length of sequence")

    # step 1 - create frequency map using hashmap
    freq_map = {}
    for i in seq:
        if i in freq_map:
            freq_map[i] = freq_map[i] + 1
        else:
            freq_map[i] = 1


    # step 2 - determine k largest in frequency map using minheap
    max_heap = []
    # first add k elements to heap
    for key,v in freq_map.items():
        heapq.heappush(max_heap, (-v,key))

    res = []
    for i in range(k):
        res.append(heapq.heappop(max_heap)[1])
    return res


def main():
    seq = [1,1,1,6,6,6,7,1,2,3,4,9,9,9,9,9]
    res = top_k_frequent_numbers(seq, 2)
    print(f'{res}')


if __name__ == "__main__":
    main()
