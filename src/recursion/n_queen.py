class Solution:
    def solveNQueens(self, n):

        result = []
        board = [['.'] * n for _ in range(n)]
        column = [0] * n
        diagonal = [0] * (2 * n)
        anti_diagonal = [0] * (2 * n)

        def helper(row):
            if row == n:
                result.append([''.join(r) for r in board])
                return

            for col in range(n):
                if column[col] + diagonal[row + col] + anti_diagonal[n - row + col] != 0:
                    continue
                board[row][col] = 'Q'
                column[col] = diagonal[row + col] = anti_diagonal[n - row + col] = 1
                helper(row + 1)
                board[row][col] = '.'
                column[col] = diagonal[row + col] = anti_diagonal[n - row + col] = 0

        helper(0)
        return result


if __name__ == "__main__":
    solution = Solution()
    n = 4 # Example with 4 queens
    solutions = solution.solveNQueens(n)

    # Print all solutions
    for sol in solutions:
        for row in sol:
            print(row)
        print()








