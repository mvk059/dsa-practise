from src.tree_binary.tree_node import TreeNode


def test_function(func, test_cases):
    # Use custom printing for TreeNode objects
    def print_tree(val):
        if isinstance(val, TreeNode):
            return val.print_tree()
        return val

    for i, test_case in enumerate(test_cases):
        # Unpack the inputs and expected output
        *inputs, expected_output = test_case

        # Call the function with unpacked inputs
        result = func(*inputs)

        print(f"Test case {i + 1}:")
        print(f"Inputs:             {list(map(print_tree, inputs))}")
        print(f"Expected Output:    {print_tree(expected_output)}")
        print(f"Actual Output:      {print_tree(result)}")

        # Assert to check if the result matches the expected output
        assert result == expected_output, f"Test case {i + 1} failed: expected {expected_output}, got {result}"
        print("Test case passed.\n")
