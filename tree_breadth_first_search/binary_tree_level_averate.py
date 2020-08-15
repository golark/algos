from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):

    result = []
    q = deque()
    q.append(root)

    while q:

        num_nodes = len(q)
        current_level = []
        for _ in range(num_nodes):
            node = q.popleft()
            current_level.append(node.val)

            # append nodes to queue
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        result.append(sum(current_level))

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


if __name__ == "__main__":
    main()
