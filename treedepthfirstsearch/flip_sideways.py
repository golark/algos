

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def flip_sideways(node):

    if node is None:
        return

    # swap
    node.left, node.right = node.right, node.left

    if node.left is not None:
        flip_sideways(node.left)
    if node.right is not None:
        flip_sideways(node.right)

    return


def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)

    flip_sideways(root)

    print(f'{root.right.right.val}')


if __name__ == "__main__":
    main()