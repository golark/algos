import heapq


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __lt__(self, other):
        return self.val < other.val

# merge_k_sorted_lists
# given k sorted linked lists, merge them into a single list
def merge_k_sorted_lists(lists):

    min_heap = []

    # push to min_heap
    for root in lists:
        heapq.heappush(min_heap, root)

    head = heapq.heappop(min_heap)
    prev_node = head

    if head.next is not None:
        heapq.heappush(min_heap, head.next)

    while min_heap:

        node = heapq.heappop(min_heap)

        if node.next is not None:
            heapq.heappush(min_heap, node.next)

        prev_node.next = node
        prev_node = node

    prev_node.next = None

    return head


def main():
    seq1 = Node(7)
    seq1.next = Node(8)
    seq1.next.next = Node(9)
    seq1.next.next = Node(11)
    seq1.next.next.next = None

    seq2 = Node(1)
    seq2.next = Node(5)
    seq2.next.next = Node(10)
    seq2.next.next = Node(19)
    seq2.next.next.next = None

    seq3 = Node(2)
    seq3.next = Node(6)
    seq3.next.next = Node(12)
    seq3.next.next = Node(16)
    seq3.next.next.next = None

    merged = merge_k_sorted_lists([seq1, seq2, seq3])
    while merged is not None:
        print(f'{merged.val}')
        merged = merged.next


if __name__ == "__main__":
    main()
