import math


# selection_sort
def selection_sort(arr):

    for i in range(len(arr)-1):

        current_min = arr[i]
        min_idx = i
        for j in range(i+1, len(arr)):

            # find minimum
            if arr[j] < current_min:
                current_min = arr[j]
                min_idx = j

        # swap minimum with i'th element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def main():

    arr = [5,6,8,1,2,4,5,10]
    selection_sort(arr)

    print(f'{arr}')


if __name__ == "__main__":
    main()
