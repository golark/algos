import ..linked_list

# returns True if linkedlist has a cycle
def has_cycle(head):

    f = head
    s = head

    while f is not None and f.next is not None:

        s = s.next
        f = f.next.next

        if f == s: # detected cycle
            return True

    return False


def main():
    pass


if __name__ == "main":
    main()
