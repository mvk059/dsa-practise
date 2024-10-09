class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def helper(n1, n2, input, found):
            if input == '' and found:
                return True

            n3 = str(n1 + n2)
            index = min(len(input), len(n3))
            if input[:index] == n3:
                return helper(n2, int(n3), input[index:], True)

            return False

        for i in range(1, n-1):
            n1 = int(num[:i])
            if str(n1) != num[:i]:
                break
            for j in range(i+1, n):
                n2 = int(num[i:j])
                if str(n2) != num[i:j]:
                    break
                found = helper(n1, n2, num[j:], False)
                if found:
                    return True
        return False


def main():
    sol = Solution()
    # result = sol.isAdditiveNumber("112358")
    # print(result)
    # print("\n")
    result = sol.isAdditiveNumber("199100199")
    print(result)


if __name__ == "__main__":
    main()
