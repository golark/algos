import math


# max_sum_of_subarray
# returns maximum of sum of subarray of size K
def max_sum_of_subarray(K, arr):
    m = -math.inf
    s = 0
    p = 0
    for i in range(len(arr)):
        s = s + arr[i]
        if i >= K-1:
            m = max(m, s)
            s = s - arr[p]
            p = p + 1

    return m


def main():
    res = max_sum_of_subarray(3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(f'{res}')


if __name__ == "__main__":
    main()
