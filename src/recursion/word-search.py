class Solution:
    def exist(self, board, word):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0]:
                    if self.helper(0, i, j, board, word):
                        return True

    def helper(self, index, i, j, board, word):
        if index == len(word):
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index]:
            return False

        temp = board[i][j]
        board[i][j] = ''

        ans = (self.helper(index + 1, i + 1, j, board, word) or
               self.helper(index + 1, i, j + 1, board, word) or
               self.helper(index + 1, i - 1, j, board, word) or
               self.helper(index + 1, i, j - 1, board, word))

        board[i][j] = temp
        return ans


def main():
    sol = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"
    if sol.exist(board, word):
        print("Word found!")
    else:
        print("Word not found!")


if __name__ == "__main__":
    main()
