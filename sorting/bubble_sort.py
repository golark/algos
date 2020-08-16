

# bubble_sort
def bubble_sort(arr):

    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]


def main():

    arr = [5,6,8,1,2,4,5,10]
    bubble_sort(arr)

    print(f'{arr}')


if __name__ == "__main__":
    main()