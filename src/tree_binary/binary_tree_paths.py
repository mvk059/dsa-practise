from typing import Optional, List

from src.tree_binary.deserialise import deserialize
from src.tree_binary.tree_node import TreeNode


def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    def helper(node, current, result):
        if node is None:
            return
        if node.left is None and node.right is None:
            current += str(node.val)
            result.append(current[:])
            return

        current += str(node.val) + "->"
        helper(node.left, current, result)
        helper(node.right, current, result)

    result = []
    current = ""
    helper(root, current, result)
    return result


def main():
    root = deserialize("1 2 3 # 5 # # # #")
    root.print_tree()

    result = binaryTreePaths(root)
    print(result)


if __name__ == "__main__":
    main()
