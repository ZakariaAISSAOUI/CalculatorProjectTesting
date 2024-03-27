import pytest
from calculate.view import View


@pytest.mark.parametrize("operation, result, expected_output", [
    ("1 + 9", 10, "RESULT : 1 + 9 = 10"),                                       # Test case where result is not None
    ("Invalid operation", None, "Your operation is wrong! : Invalid operation")  # Test case where result is None
])
def test_print_result(operation, result, expected_output, capsys):
    # Call the function under test
    View.print_result(operation, result)

    # Capture the printed output
    captured = capsys.readouterr()

    # Assertion: Check if the captured output matches the expected output for each test case
    assert captured.out.strip() == expected_output
