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


def main():
    prices = [6,1,0,10,9,8]
    res = maximum_profit(prices)
    print(f'{res}')

if __name__ == "__main__":
    main()
