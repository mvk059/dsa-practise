from typing import Optional, List

from src.recursion.treenode import TreeNode


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

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
    sol = Solution()
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    five = TreeNode(5)

    one.left = two
    one.right = three
    two.right = five

    result = sol.binaryTreePaths(one)
    print(result)


if __name__ == "__main__":
    main()
