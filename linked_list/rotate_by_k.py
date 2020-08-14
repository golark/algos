import linkedlist


def rotate_by_k(llist, k):

    section_head = llist.head
    section_tail = None

    n = llist.head
    i = 0
    while n.next is not None:
        i = i + 1
        if i == k: # find section tail
            section_tail = n

            # set new head
            llist.head = section_tail.next

        n = n.next

    n.next = section_head
    section_tail.next = None


def main():
    llist = linkedlist.SingleLinkedList()

    for i in range(10):
        llist.append(i)
    rotate_by_k(llist,4)

    llist.display()


if __name__ == "__main__":
    main()
