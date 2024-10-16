from collections import deque
from typing import Optional

from src.test_helper import test_function
from src.tree_binary.deserialise import deserialize
from src.tree_binary.tree_node import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    def helper(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        if not node.left and not node.right:
            return 1
        return max(helper(node.left), helper(node.right)) + 1

    def helper_iter(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        queue = deque()
        queue.append(node)
        level = 0

        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            level += 1

        return level

    return helper_iter(root)


def main():
    root1 = deserialize("3 9 20 # # 15 7 # # # #")

    # Last value is the expected output
    test_cases = [
        (root1, 3),
    ]
    test_function(max_depth, test_cases)


if __name__ == '__main__':
    main()
