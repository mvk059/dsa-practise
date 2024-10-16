from typing import Optional

from src.test_helper import test_function
from src.tree_binary.deserialise import deserialize
from src.tree_binary.tree_node import TreeNode


def is_balanced(root: Optional[TreeNode]) -> bool:
    result = True

    def helper(node):
        if not node:
            return 0
        if node.left is None and node.right is None:
            return 1

        left = helper(node.left)
        right = helper(node.right)

        if abs(left - right) > 1:
            result = False

        return max(left, right) + 1

    helper(root)
    return result


def main():
    root1 = deserialize("3 9 20 # # 15 7 # # # #")

    # Last value is the expected output
    test_cases = [
        (root1, 3),
    ]
    test_function(is_balanced, test_cases)


if __name__ == '__main__':
    main()
