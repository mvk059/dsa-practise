class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        i = 0
        while i < len(A) - 1:
            A[i], A[i + 1] = A[i + 1], A[i]
            i += 2

        return A


def main():
    sol = Solution()
    result = sol.wave([5, 1, 3, 2, 4])
    print(result)


if __name__ == "__main__":
    main()
