

# pair_with_target_sum
# given sorted array find pair that is equal to target_sum
# return element indexes
def pair_with_target_sum(arr, target_sum):

    p = 0
    q = len(arr)-1

    while q > p:
        current_sum = arr[p] + arr[q]
        if current_sum == target_sum:
            return [p, q]
        elif current_sum > target_sum:
            q = q - 1
        else:
            p = p + 1


def main():
    nums = [1,2,3,4,5,6,7,8,9,10]
    res = pair_with_target_sum(nums, 5)
    print(f'{res}')


if __name__ == "__main__":
    main()
