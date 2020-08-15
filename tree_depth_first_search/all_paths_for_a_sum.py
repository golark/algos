

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# path_sum
# return True if there is a path with the given sum s
def all_paths_for_sum(root, s):

    # return condition
    # if leaf node and sum is zero
    if root is None:
        return 0
    if root.left is None and root.right is None:
        if s == root.val:
            return 1

    # recurse
    return all_paths_for_sum(root.left, s - root.val) + all_paths_for_sum(root.right, s-root.val)


def main():
    root = TreeNode(1)
    root.left = TreeNode(7)
    root.right = TreeNode(9)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(7)

    res = all_paths_for_sum(root, 12)
    print(f'{res}')


if __name__ == "__main__":
    main()