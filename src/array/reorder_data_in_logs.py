from src.test_helper import test_function


def reorder_logs(logs):
    letter_logs = []
    digit_logs = []

    # Separate the logs into letter-logs and digit-logs
    for log in logs:
        identifier, *content = log.split("-")
        if content[0].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append((identifier, '-'.join(content)))

    # Sort the letter-logs
    letter_logs.sort(key=lambda x: (x[1], x[0]))

    # Reconstruct the final output
    sorted_letter_logs = [f"{identifier}-{content}" for identifier, content in letter_logs]
    return sorted_letter_logs + digit_logs


def main():
    # Last value is the expected output
    test_cases = [
        (["dig1-8-1-5-1", "let1-art-can", "dig2-3-6", "let2-own-kit-dig", "let3-art-zero"],
         ["let1-art-can", "let3-art-zero", "let2-own-kit-dig", "dig1-8-1-5-1", "dig2-3-6"]),
    ]
    test_function(reorder_logs, test_cases)


if __name__ == '__main__':
    main()
