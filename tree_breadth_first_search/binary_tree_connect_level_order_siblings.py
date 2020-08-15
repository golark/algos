from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def traverse(root):

    result = []
    q = deque()
    q.append(root)


    while q:

        num_nodes = len(q)
        for _ in range(num_nodes):
            node = q.popleft()

            if node is root:
                head = Node(root.val)
                prev_node = head
            else:
                prev_node.next = Node(node.val)
                prev_node = prev_node.next

            # append nodes to queue
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    prev_node.next = None

    return head


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    res = traverse(root)

    while res:
        print(f'{res.val}')
        res = res.next


if __name__ == "__main__":
    main()
