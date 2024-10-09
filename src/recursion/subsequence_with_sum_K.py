def checkSubsequenceSum(nums, k):
    def helper(index: int, k: int, nums: list) -> bool:
        if k == 0:
            return True
        if k < 0:
            return False
        if index == len(nums):
            return k == 0

        pick = helper(index + 1, k - nums[index], nums)
        if pick:
            return True
        not_pick = helper(index + 1, k, nums)

        return pick or not_pick

    return helper(0, k, nums)


def main():
    nums = [1, 10, 4, 5]
    k = 16
    print(checkSubsequenceSum(nums, k))


if __name__ == '__main__':
    main()
