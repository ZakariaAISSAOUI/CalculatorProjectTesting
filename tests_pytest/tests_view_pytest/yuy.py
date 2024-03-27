from calculate.view import View
#  == f"RESULT : {operation} = {result}"


def print_result(operation, result):

    if result is not None:
        print(f"RESULT : {operation} = {result}")
    else:
        print(f"Your operation is wrong! : {operation}")


print_result('2 + 3', 5)


def printing_result_valid_operation():
    operation = "1 + 9"
    result = 10
    return View.print_result(operation, result)


a = View.print_result("9 + 9", 19)
print(a)