class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 10:
            return 10

        self.count = 0
        nums = [0,1,2,3,4,5,6,7,8,9]

        def helper(current):
            if len(current) <= n:
                if current and current[0] != 0:
                    self.count += 1
            else:
                return

            for num in nums:
                if num not in current:
                    current.append(num)
                    helper(current)
                    current.pop()

        helper([])
        return self.count + 1


def main():
    sol = Solution()
    result = sol.countNumbersWithUniqueDigits(2)
    print(result)


if __name__ == "__main__":
    main()
