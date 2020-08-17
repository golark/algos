

# sort given sequence given that the numbers go from 1 to n
def cyclic_sort(seq):
    for i in range(len(seq)):
        num = seq[i]
        if num != seq[num-1]:
            # swap
            seq[num-1], seq[i] = seq[i], seq[num-1]


def main():
    seq = [5,4,1,2,3]
    cyclic_sort(seq)

    print(f'seq = {seq}')


if __name__ == "__main__":
    main()
