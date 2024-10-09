def combination_sum2(candidates, target):

    def helper(index, target, nums, current, result):
        if target == 0:
            result.append(current[:])
            return

        if target < 0 or index == len(nums):
            return

        # pick
        current.append(nums[index])
        helper(index + 1, target - nums[index], nums, current, result)
        current.pop()

        # not pick
        for next_index in range(index + 1, len(nums)):
            if nums[index] != nums[next_index]:
                helper(next_index, target, nums, current, result)
                break

    candidates.sort()
    current = []
    result = []
    helper(0, target, candidates, current, result)
    return result


def main():
    candidates = [2, 1, 2, 7, 6, 1, 5]
    target = 8
    print(combination_sum2(candidates, target))


if __name__ == '__main__':
    main()
