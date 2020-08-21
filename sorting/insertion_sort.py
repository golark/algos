

# insertion_sort
def insertion_sort(arr):

    for i in range(1, len(arr)):

        # find the correct location by swapping
        idx = i
        while idx > 0 and arr[idx] < arr[idx-1]:
            arr[idx-1], arr[idx] = arr[idx], arr[idx-1]
            idx = idx - 1


def main():

    arr = [5,6,8,1,2,4,5,10]
    insertion_sort(arr)

    print(f'{arr}')


if __name__ == "__main__":
    main()
