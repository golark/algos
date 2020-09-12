
class Node:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None


# given BST, return a list of branch sums from left to right
def branch_sums(node):

    sums = []
    def _branch_sums(node, sums, current_sum):

        if node is None:
            return

        if node.left is None and node.right is None:
            sums.append(node.val+current_sum)
            return

        _branch_sums(node.left, sums, current_sum+node.val)
        _branch_sums(node.right, sums, current_sum+node.val)

        return

    _branch_sums(node, sums, 0)
    return sums


def main():
    root = Node(10)
    root.left = Node(7)
    root.right = Node(12)
    root.left.left = Node(1)
    root.left.right = Node(8)
    root.right.left = Node(6)
    root.right.right = Node(15)
    res = branch_sums(root)

    print(f'{res}')


if __name__ == "__main__":
    main()