

# returns nth fibonacci number
# recursive implementation
# fibonacci sequence: 0 - 1 - 1 - 2 - 3 - 5
# n = 1, res = 0
# n = 2, res = 1
def nth_fibonacci(n):

    # return condition
    if n == 1:
        return 0
    if n == 2:
        return 1

    return nth_fibonacci(n-1) + nth_fibonacci(n-2)


def main():

    res = nth_fibonacci(5)
    print(f'{res}')


if __name__ == "__main__":
    main()