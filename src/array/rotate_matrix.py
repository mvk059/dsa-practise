from typing import List

from src.test_helper import test_function


# TC: O(N * M)
# SC: O(1)
def rotate(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

    return matrix


def main():
    # Last value is the expected output
    test_cases = [
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    ]
    test_function(rotate, test_cases)


if __name__ == '__main__':
    main()
