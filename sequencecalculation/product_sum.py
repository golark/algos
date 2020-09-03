

# product_sum
# [x+y]=x+y
# [x, [y,z]]=x+2*(y+z)
def product_sum(seq):

    def _product_sum(seq, nest_level):

        # return condition
        s = 0
        for k,i in enumerate(seq):
            if isinstance(i, list):
                s = s + _product_sum(seq[k], nest_level+1)
            else:
                s = s + nest_level * i

        return s

    return _product_sum(seq, 1)


def main():
    res = product_sum([1,[2,3,[4,5]]])
    print(f'{res}')


if __name__ == "__main__":
    main()
