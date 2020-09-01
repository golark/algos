import linkedlist


def inplace_reverse(llist):

    p = None
    n = llist.head

    while n is not None:

        # reverse current node
        next_node = n.next
        n.next = p

        # move to next node
        p = n
        n = next_node

    llist.head = p


def main():
    llist = linkedlist.SingleLinkedList()

    for i in range(10):
        llist.append(i)
    inplace_reverse(llist)

    llist.display()


if __name__ == "__main__":
    main()
