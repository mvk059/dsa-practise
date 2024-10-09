from src.test_helper import test_function


# @param A : tuple of integers
# @return an integer
# TC: O(N)
# SC: O(1)
def max_sub_array(nums):
    curr_sum = 0
    max_sum = float('-inf')
    for num in nums:
        curr_sum += num
        max_sum = max(max_sum, curr_sum)
        if curr_sum <= 0:
            curr_sum = 0
    return max_sum


def main():
    # Last value is the expected output
    test_cases = [
        ([1, 2, 3, 4, -10], 10),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-500], -500),
        ([-500, -20], -20),
    ]
    test_function(max_sub_array, test_cases)


if __name__ == '__main__':
    main()
