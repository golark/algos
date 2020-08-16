

# quick_sort
# choose a pivot, set 2 new lists with elements lower/higher than the pivot
# sort the left/right lists
def quick_sort(arr):

    # return condition
    if len(arr) <= 1:
        return arr

    # choose a pivot
    pivot = arr.pop()

    l_list = []
    r_list = []
    for item in arr:
        if item > pivot:
            r_list.append(item)
        else:
            l_list.append(item)

    return quick_sort(l_list) + [pivot] + quick_sort(r_list)


def main():

    arr = [15,6,8,1,2,4,10,5]
    arr = quick_sort(arr)

    print(f'{arr}')


if __name__ == "__main__":
    main()