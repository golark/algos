import heapq


# find_k_largest_numbers
#  heap based approach
def find_k_largest_numbers(nums, k):
    min_heap = []

    for i in range(k):
        heapq.heappush(min_heap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap,nums[i])

    return min_heap


def main():

    seq = [1,4,5,10,0,1,2,5,2,15,19,21]
    res = find_k_largest_numbers(seq, 3)

    print(f'{res}')


if __name__ == "__main__":
    main()