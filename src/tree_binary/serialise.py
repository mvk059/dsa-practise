from typing import Optional

from src.tree_binary.tree_node import TreeNode


def serialise(root: Optional[TreeNode]):
    def helper(node: Optional[TreeNode]):
        if node:
            result.append(str(node.val))
            helper(node.left)
            helper(node.right)
        else:
            result.append("#")

    result = []
    helper(root)
    return ' '.join(result)


def main():
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    five = TreeNode(5)

    one.left = two
    one.right = three
    two.right = five

    result = serialise(one)
    print(result)


if __name__ == "__main__":
    main()
