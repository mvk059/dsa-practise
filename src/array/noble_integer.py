from src.test_helper import test_function


def noble_integer(nums):
    nums.sort()
    n = len(nums)

    for i in range(n - 1):
        if nums[i] == nums[i + 1]:
            continue
        if nums[i] == n - 1 - i:
            return 1

    return 1 if nums[n - 1] == 0 else -1


def main():
    # Last value is the expected output
    test_cases = [
        ([3, 2, 1, 3], 1),
        ([1, 1, 3, 3], -1),
        ([0, 0, 0], 1),
    ]
    test_function(noble_integer, test_cases)


if __name__ == '__main__':
    main()
