from typing import List

from src.test_helper import test_function


# TC: O(N + MLogM), N: counting occurrences, M: number of unique elements in A
# SC: O(M + M), M: number of unique elements in A
def find_occurrences1(nums: List[int]) -> List[int]:
    counter = {}
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1
    counter_sorted = sorted(counter.keys())
    return [counter[key] for key in counter_sorted]


# TC: O(NLogN), N: input
# SC: O(M), M: number of unique elements in A
def find_occurrences2(nums: List[int]) -> List[int]:
    nums.sort()
    n = len(nums)
    result = []
    i = 0

    while i < n:
        current = nums[i]
        count = 0
        while i < n and nums[i] == current:
            count += 1
            i += 1
        result.append(count)

    return result


def main():
    # Last value is the expected output
    test_cases = [
        ([4, 3, 3], [2, 1]),
    ]
    test_function(find_occurrences1, test_cases)
    test_function(find_occurrences2, test_cases)


if __name__ == '__main__':
    main()
