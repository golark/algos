import math


def maximum_profit(prices):

    if len(prices) < 2:
        raise ValueError('Require at least 2 entries')

    p = 1
    max_profit = -math.inf
    min_purchase = prices[0]

    for i in range(len(prices)-1):

        # check if max_profit
        if prices[p] - min_purchase > max_profit:
            max_profit = prices[p] - min_purchase

        if prices[p] < min_purchase:
            min_purchase = prices[p]

        p = p + 1

    return max_profit


# maximum_profit2
# prices are sampled per time unit transaction
# determine the maximum profit that can be obtained
# sliding window approach ( window size of 2 )
# O(n) time complexity and O(1) space
def maximum_profit2(prices):

    if prices is None:
        return
    if len(prices) < 2:
        raise ValueError("length of prices is less than 2")

    prev = prices[0]
    min_purchase = prices[0]
    max_profit = -math.inf
    for k in range(1,len(prices)):

        # update min_purchase price
        if prev < min_purchase:
            min_purchase = prev

        # update max_profit
        profit = prices[k] - min_purchase
        if profit > max_profit:
            max_profit = profit

        prev = prices[k]

    return max_profit


def main():
    prices = [-1,6,1,0,1,12,9,8]
    res = maximum_profit2(prices)
    print(f'{res}')


if __name__ == "__main__":
    main()
