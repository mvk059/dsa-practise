def test_function(func, test_cases):
    for i, test_case in enumerate(test_cases):
        # Unpack the inputs and expected output
        *inputs, expected_output = test_case

        # Call the function with unpacked inputs
        result = func(*inputs)

        print(f"Test case {i + 1}:")
        print(f"Inputs:             {inputs}")
        print(f"Expected Output:    {expected_output}")
        print(f"Actual Output:      {result}")

        # Assert to check if the result matches the expected output
        assert result == expected_output, f"Test case {i + 1} failed: expected {expected_output}, got {result}"
        print("Test case passed.\n")