def partition(s: str):
    def helper(index, input, current, result):
        if index == len(input):
            result.append(current[:])
            return

        for end_index in range(index, len(input)):
            if not is_palindrome(input, index, end_index):
                continue
            current.append(input[index:end_index + 1])
            helper(end_index + 1, input, current, result)
            current.pop()

    def is_palindrome(input, start, end):
        while start < end:
            if input[start] != input[end]:
                return False
            start += 1
            end -= 1
        return True

    result = []
    helper(0, s, [], result)
    return result


def main():
    result = partition("aabaa")
    print(result)


if __name__ == "__main__":
    main()
