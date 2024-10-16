from typing import Optional

from src.test_helper import test_function
from src.tree_binary.deserialise import deserialize
from src.tree_binary.tree_node import TreeNode


def is_symmetric(root: Optional[TreeNode]) -> bool:
    def helper(one: Optional[TreeNode], two: Optional[TreeNode]) -> bool:
        if one is None and two is None:
            return True
        if one is None or two is None:
            return False
        if one.val != two.val:
            return False
        return helper(one.left, two.right) and helper(one.right, two.left)

    return helper(root, root)


def main():
    root1 = deserialize("1 2 2 3 4 4 3 # # # # # # # #")
    root2 = deserialize("1 2 2 # 3 # 3 # # # #")

    # Last value is the expected output
    test_cases = [
        (root1, True),
        (root2, False),
    ]
    test_function(is_symmetric, test_cases)


if __name__ == '__main__':
    main()
