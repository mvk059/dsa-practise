from typing import Optional

from src.test_helper import test_function
from src.tree_binary.deserialise import deserialize
from src.tree_binary.tree_node import TreeNode


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def main():
    root1 = deserialize("1 2 3 # # # #")
    root2 = deserialize("1 2 3 # # # #")
    root3 = deserialize("1 2 # # #")
    root4 = deserialize("1 # 2 # #")

    # Last value is the expected output
    test_cases = [
        (root1, root2, True),
        (root3, root4, False),
    ]
    test_function(is_same_tree, test_cases)


if __name__ == '__main__':
    main()
