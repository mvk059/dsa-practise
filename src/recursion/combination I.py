def combination_sum(candidates, target):

    def helper(index, target, nums, current, result):
        if target == 0:
            result.append(current[:])
            return

        if target < 0 or index == len(nums):
            return

        # pick
        current.append(nums[index])
        helper(index, target - nums[index], nums, current, result)
        current.pop()

        # not pick
        helper(index + 1, target, nums, current, result)

    current = []
    result = []
    helper(0, target, candidates, current, result)
    return result


def main():
    candidates = [2, 3, 5, 4]
    target = 7
    print(combination_sum(candidates, target))


if __name__ == '__main__':
    main()
