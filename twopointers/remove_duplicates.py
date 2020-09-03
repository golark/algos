

# remove duplicates from sorted list
def remove_duplicates(arr):

    new_list = []

    p = 0
    q = 1

    new_list.append(arr[p])
    while q < len(arr):

        if arr[p] != arr[q]:
            p = q
            new_list.append(arr[p])

        q = q + 1

    return new_list


def main():
    arr = [1,2,3,3,3,3,4,4,4,4,5,5,5,5,6]
    res = remove_duplicates(arr)
    print(f'{res}')


if __name__ == "__main__":
    main()