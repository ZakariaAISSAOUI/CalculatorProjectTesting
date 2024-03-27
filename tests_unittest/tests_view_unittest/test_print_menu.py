from calculate.view import View


def test_should_print_menu(capsys):
    View.print_menu()
    captured = capsys.readouterr()
    expect_out = ("\n=========== MENU ==========="
                  "\n1 - Addition"
                  "\n2 - Subtraction"
                  "\n3 - Multiplication"
                  "\n4 - Division"
                  "\n5 - Exit"
                  "\n============================\n\n")
    assert captured.out == expect_out
