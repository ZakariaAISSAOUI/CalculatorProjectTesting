import unittest
from io import StringIO
import contextlib
from calculate.view import View


class TestView(unittest.TestCase):
    def setUp(self):
        self.string = StringIO()

    def test_should_print_menu(self):
        with contextlib.redirect_stdout(self.string):
            View.print_menu()

        output = self.string.getvalue()
        expect_out = ("\n=========== MENU ==========="
                      "\n1 - Addition"
                      "\n2 - Subtraction"
                      "\n3 - Multiplication"
                      "\n4 - Division"
                      "\n5 - Exit"
                      "\n============================\n\n")
        self.assertEqual(output, expect_out)

    def test_should_print_end_message(self):
        with contextlib.redirect_stdout(self.string):
            View.end_message()

        output = self.string.getvalue()
        expect_out = '=========== GOOD-BYE ===========\n'
        self.assertEqual(output, expect_out)

    def test_print_result(self):
        with contextlib.redirect_stdout(self.string):
            operation = "1 + 8"
            result = 9
            View.print_result(operation, result)

        # Capture the printed output
        outPut = self.string.getvalue().strip()

        # Define the expected output
        expectOut = f"RESULT : {operation} = {result}"

        # Assert printed output matches expected output
        self.assertEqual(outPut, expectOut)

    def test_should_print_result_with_error(self):
        with contextlib.redirect_stdout(self.string):
            operation = "A + 8 + ^"
            result = None
            View.print_result(operation, result)

        outPut = self.string.getvalue().strip()
        expectOut = f"Your operation is wrong! : {operation}"
        self.assertEqual(outPut, expectOut)


if __name__ == "__main__":
    unittest.main()
