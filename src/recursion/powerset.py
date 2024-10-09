def power_set(nums):

    def pset(index: int, nums: list, current: list, result: list):
        if index == len(nums):
            result.append(current[:])
            return

        # not pick
        pset(index + 1, nums, current, result)

        # pick
        current.append(nums[index])
        pset(index + 1, nums, current, result)
        current.pop()

    result = []
    current = []
    pset(0, nums, current, result)
    return result


def main():
    result = power_set([1, 2, 3])
    print(result)


if __name__ == "__main__":
    main()
