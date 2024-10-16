from collections import deque
from typing import Optional

from src.tree_binary.tree_node import TreeNode


def deserialize(data: str) -> Optional[TreeNode]:
    if not data:
        return
    values = data.split()
    n = len(values)
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    # when you pop a node, its children will be at i and i+1
    while queue:
        node = queue.pop()
        if i < n and values[i] != '#':
            node.left = TreeNode(int(values[i]))
            queue.appendleft(node.left)
        i += 1
        if i < n and values[i] != '#':
            node.right = TreeNode(int(values[i]))
            queue.appendleft(node.right)
        i += 1
    return root


def main():
    input = "1 2 3 # # 4 5 # # # #"

    result = deserialize(input)
    result.print_tree()


if __name__ == "__main__":
    main()
