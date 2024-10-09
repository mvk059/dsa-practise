def powersetII(nums):
    def helper(index, nums, current, result):
        if index == len(nums):
            result.append(current[:])
            return

            # pick
        current.append(nums[index])
        helper(index + 1, nums, current, result)
        current.pop()

        # not pick
        for next_index in range(index + 1, len(nums)):
            if nums[index] != nums[next_index]:
                helper(next_index, nums, current, result)
                return

                # all duplicates at the end
        helper(len(nums), nums, current, result)

    nums.sort()
    current = []
    result = []
    helper(0, nums, current, result)
    return result


def main():
    result = powersetII([1, 3, 3])
    print(result)


if __name__ == "__main__":
    main()
