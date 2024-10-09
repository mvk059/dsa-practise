from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def helper(index, n, length):
            if len(current) == length:
                result.append(current[:])
                return

            for i in range(index, n + 1):
                current.append(i)
                helper(i + 1, n, length)
                current.pop()

        result = []
        current = []
        helper(1, n, k)
        return result


def main():
    sol = Solution()
    n = 4
    k = 2
    print(sol.combine(n, k))


if __name__ == '__main__':
    main()
