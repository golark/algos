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


# rotate_left_by_k
# O(n)
# step 1 - find sub list head and tail
# step 2 - set new head and tail

#
#          k = 5
#           v ( new head )
#         a b
# _ _ _ _ _ _ _ _ _ -> None
#
#
# b               a
# _ _ _ _ _ _ _ _ _ -> None
def rotate_left_by_k(llist, k):

    # step 1 - find sublist head and tail
    node = llist.head
    for i in range(k-1):
        if node is None:
            raise IndexError("rotation count " + str(k) + " is larger than the length of the llist")
        node = node.next
    sublist_tail = node

    # check if we are at tail, in that case no need to rotate
    if sublist_tail is None:
        return
    new_head = sublist_tail.next

    # traverse to the previous tail
    while node.next is not None:
        node = node.next
    tail = node

    # step 2 - set new head and tail
    tail.next = llist.head
    llist.head = new_head
    sublist_tail.next = None


# rotate_right_by_k
# step 1 - find subsection head ( k'th node before tail )
# step 2 - adjust references for rotation
# O(n)
def rotate_right_by_k(llist, k):

    if k == 0:
        return

    # step 1 - find subsection tail
    node = llist.head
    new_tail = node
    i = 0
    while node.next is not None:
        i = i + 1
        if i > k:
            new_tail = new_tail.next
        node = node.next
    tail = node

    # step 2 - adjust references
    tail.next = llist.head
    llist.head = new_tail.next
    new_tail.next = None


def main():
    llist = linkedlist.SingleLinkedList()

    for i in range(10):
        llist.append(i)
    rotate_left_by_k(llist, 1)
    rotate_right_by_k(llist, 1)

    llist.display()


if __name__ == "__main__":
    main()
