from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def helper(index, nums, current, result) -> int:

            if index == len(nums):
                if len(current) == 0:
                    return result
                sum = current[0]
                for i in range(1, len(current)):
                    sum ^= current[i]
                result += sum
                return result

            # not pick
            result = helper(index + 1, nums, current, result)

            # pick
            current.append(nums[index])
            result = helper(index + 1, nums, current, result)
            current.pop()

            return result

        result = 0
        current = []
        return helper(0, nums, current, result)


def main():
    sol = Solution()
    result = sol.subsetXORSum([1, 3])
    print(result)
    print("\n")
    result = sol.subsetXORSum([5, 1, 6])
    print(result)


if __name__ == "__main__":
    main()
