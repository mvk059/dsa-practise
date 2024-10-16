from typing import Optional, List

from src.tree_binary.deserialise import deserialize
from src.tree_binary.tree_node import TreeNode


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []

    def helper(node: Optional[TreeNode]):
        if node is None:
            return

        helper(node.left)
        result.append(node.val)
        helper(node.right)

    helper(root)
    return result


def main():
    root = deserialize("1 2 3 # 5 # # # #")
    root.print_tree()
    result = inorder_traversal(root)
    print(result)


if __name__ == "__main__":
    main()
