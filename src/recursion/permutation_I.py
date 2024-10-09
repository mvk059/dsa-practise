from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def helper(start, end):
            if start == end:
                result.append(nums[:])
                return

            for i in range(start, end):
                # Swap the current element with the starting element
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse on the next part of the array
                helper(start + 1, end)
                # Backtrack (swap back)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        helper(0, len(nums))
        return result


def main():
    sol = Solution()
    result = sol.permute([1, 2, 3])
    print(result)


if __name__ == "__main__":
    main()

