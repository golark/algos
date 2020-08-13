# sums_of_subarray
# find sums of subarrays each of length K
def sums_of_subarray(K, arr):
    # pre loop
    res = []
    s = 0
    for i in range(K):
        s = s + arr[i]
    res.append(s)

    # main loop
    p = 0
    for q in range(K, len(arr)):
        s = s + arr[q] - arr[p]
        res.append(s)
        p = p + 1
        q = q + 1

    return res


def main():
    res = sums_of_subarray(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(f'{res}')


if __name__ == "__main__":
    main()
