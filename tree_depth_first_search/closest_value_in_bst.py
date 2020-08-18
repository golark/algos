

class Node:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None


# given a BST and a target sum, find closest value to target
def closest_value_in_bst(node, target):

    # return condition
    if node is None:
        return target
    if node.left is None and node.right is None:
        return target - node.val

    return target - min(abs(closest_value_in_bst(node.left, target-node.val)), abs(closest_value_in_bst(node.right, target-node.val)))


def main():
    root = Node(10)
    root.left = Node(7)
    root.right = Node(12)
    root.left.left = Node(1)
    root.left.right = Node(8)
    root.right.left = Node(6)
    root.right.right = Node(15)
    res = closest_value_in_bst(root, 14)

    print(f'{res}')


if __name__ == "__main__":
    main()