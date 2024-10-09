def countSubsequenceWithTargetSum(nums, k):
    def helper(index: int, k: int, nums: list) -> int:
        if k == 0:
            return 1
        if k < 0:
            return 0
        if index == len(nums):
            return 1 if k == 0 else 0

        pick = helper(index + 1, k - nums[index], nums)
        not_pick = helper(index + 1, k, nums)

        return pick + not_pick

    return helper(0, k, nums)


def main():
    nums = [1, 10, 4, 5]
    k = 16
    print(countSubsequenceWithTargetSum(nums, k))


if __name__ == '__main__':
    main()
