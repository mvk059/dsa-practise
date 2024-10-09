def letter_combinations(digits):
    def helper(index, digits, map, curr, result):
        if index == len(digits):
            result.append(curr[:])
            return

        char = map[int(digits[index])]
        for ch in char:
            helper(index + 1, digits, map, curr + ch, result)

    map = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    result = []
    helper(0, digits, map, "", result)
    return result


def main():
    result = letter_combinations("34")
    print(result)


if __name__ == "__main__":
    main()
