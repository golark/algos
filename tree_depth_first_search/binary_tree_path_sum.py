

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# path_sum
# return True if there is a path with the given sum s
def path_sum(root, s):

    # return condition
    # if leaf node and sum is zero
    if root is None:
        return False
    if root.left is None and root.right is None:
        return s-root.val == 0

    # recurse
    return path_sum(root.left, s - root.val) or path_sum(root.right, s-root.val)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    res = path_sum(root, 28)
    print(f'{res}')


if __name__ == "__main__":
    main()