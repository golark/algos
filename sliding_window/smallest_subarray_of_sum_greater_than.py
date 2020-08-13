

# smallest_subarray_of_sum_greater_than
# smallest subarray whose sum is greater than S
def smallest_subarray_of_sum_greater_than(S, arr):

    smallest = len(arr)
    q = 0
    s = 0
    for p in range(len(arr)):
        s = s + arr[p]

        # increment q until
        while s >= S:
            smallest = min(smallest, p - q + 1)
            s = s - arr[q]
            q = q + 1

    return smallest


def main():
    res = smallest_subarray_of_sum_greater_than(20, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(f'{res}')


if __name__ == "__main__":
    main()