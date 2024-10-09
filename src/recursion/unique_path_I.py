class Solution:
    def findPath(self, grid):
        n = len(grid) - 1
        m = len(grid[0]) - 1

        if grid[0][0] == 0 or grid[n][m] == 0:
            return []

        def helper(i, j, current, result):
            if i == n and j == m:
                result.append(current[:])
                return

            if grid[i][j] != 1:
                return

            grid[i][j] = 0

            if i < n:
                helper(i + 1, j, current + 'D', result)
            if j < m:
                helper(i, j + 1, current + 'R', result)
            if i > 0:
                helper(i - 1, j, current + 'U', result)
            if j > 0:
                helper(i, j - 1, current + 'L', result)

            grid[i][j] = 1

        result = []
        current = ""
        helper(0, 0, current, result)
        return result


if __name__ == "__main__":
    sol = Solution()
    grid = [
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 0, 0, 1],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 1]
    ]
    # grid = [
    #     [1, 0],
    #     [1, 0],
    # ]

    paths = sol.findPath(grid)

    for path in paths:
        print(path + '\n')
