from calculate.view import View


def test_should_print_end_message(capsys):
    View.end_message()
    captured = capsys.readouterr()
    expect_out = "=========== GOOD-BYE ===========\n"
    assert captured.out == expect_out
