

# number_of_ways_for_returning_change
# approach: iterate through each of the denominator in denoms
# determine if the remainder can be dissected by the rest of the denominations
# O(n^2) time and O(1) space
def number_of_ways_for_returning_change(denoms, target):

    num_ways = 0
    for i in range(len(denoms)):

        rem = target % denoms[i]
        for j in range(i, len(denoms)):
            rem = rem % denoms[j]
            if rem == 0:
                rem = target % denoms[i]
                num_ways = num_ways + 1

    return num_ways


def main():
    denoms = [1,5]
    target = 6

    res = number_of_ways_for_returning_change(denoms, target)

    print(f'{res}')


if __name__ == "__main__":
    main()